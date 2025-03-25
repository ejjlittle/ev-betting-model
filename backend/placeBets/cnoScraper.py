import requests
from bs4 import BeautifulSoup
import shared.constants as constants
from pprint import pprint

#--GET VIEWSTATE AND VALIDATION PAYLOAD VALUES--#
def getSessionVals(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    return {
        "__VIEWSTATE": soup.find("input", {"name": "__VIEWSTATE"})["value"],
        "__EVENTVALIDATION": soup.find("input", {"name": "__EVENTVALIDATION"})["value"]
    }


#--PARSE HTML INTO DATA--#
def htmlParse(content):
    soup = BeautifulSoup(content, "html.parser")

    data = [] #list of dicts
    htmlBody = soup.find("tbody")

    if not htmlBody:
        return data #return empty if no bets able to be scraped

    for entry in htmlBody.find_all("tr"):
        categories = entry.find_all("td")
        bet = {
            "EV": float(categories[0].text[:-1]), #expected value as percentage
            "Date": entry.find('datetime')['utc'], #eg. 1/24/2025 7:30:00 PM (utc)
            "Sport": categories[4].text, #eg. Basketball
            "League": categories[5].text, #eg. NBA
            "Game": categories[6].text, #eg. Milwaukee Bucks @ Golden State Warriors
            "Market": categories[7].text, #eg. Player Threes
            "BetName": categories[8].text, #eg. Stephen Curry Over 2.5
            "Odds": categories[9].text, #eg. -170
            "Book": categories[10].text, #eg. DraftKings
            "FairOdds": categories[11].text, #eg. -200
            "BookCount": int(categories[12].text) #number of books where bet is available
        }
        data.append(bet)
    return data


#--FILTER DATA BASED ON MODEL CONSTANTS--#
def filterData(data, minEv, maxEv, leagues, books, minBooks):
    for i in range(len(data)): #filter by min EV
        if data[i]["EV"] < minEv:
            data = data[:i]
            break

    index = 0
    for i in range(len(data)): #filter by max EV
        if data[i]["EV"] <= maxEv:
            break #common case is that every EV is below the max
        else:
            index = i + 1
    data = data[index:]

    data = [entry for entry in data if entry["League"] in leagues] #filter by league
    data = [entry for entry in data if entry["Book"] in books] #filter by book
    data = [entry for entry in data if entry["BookCount"] >= minBooks] #filter by book count
    return data


def main(minEv, maxEv, leagues, books, minBooks):
    session = requests.Session()

    #get dyanimic payload values
    validation = getSessionVals(session, constants.CNO_URL)
    payload = constants.CNO_DATA.copy() 
    payload.update(validation)

    #get html response from CNO post request
    response = session.post(constants.CNO_URL, 
                            headers=constants.CNO_HEADERS,
                            data=payload)

    #check requests connection
    if response.status_code != 200:
        exit("Error fetching website data")

    data = htmlParse(response.text)
    data = filterData(data, minEv, maxEv, leagues, books, minBooks)
    return data


if __name__ == "__main__":
    data = main(7, 40, ["NBA", "NHL", "NFL", "NCAAB", "NCAAF"], ["FanDuel", "DraftKings", "BetMGM"], 5)
    pprint(data) #for dev