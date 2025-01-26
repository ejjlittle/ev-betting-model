import requests
from bs4 import BeautifulSoup
from constants import URL, HEADERS, COOKIES, DATA, MINIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT

#--PARSE HTML INTO DATA--#
def htmlParse(content):
    soup = BeautifulSoup(content, "html.parser")

    data = [] #list of dicts
    html_table = soup.find("tbody")
    for entry in html_table.find_all("tr"):
        categories = entry.find_all("td")
        bet = {
            "EV": float(categories[0].text[:-1]), #expected value as percentage
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
def filterData(data):
    for i in range(len(data)): #filter by EV
        if data[i]["EV"] < MINIMUM_EV_PERCENTAGE:
            data = data[:i]
            break
    data = [entry for entry in data if entry["League"] in LEAGUES] #filter by league
    data = [entry for entry in data if entry["Book"] in BOOKS] #filter by book
    data = [entry for entry in data if entry["BookCount"] >= MINIMUM_BOOK_COUNT] #filter by book count
    return data


response = requests.post(URL, headers=HEADERS,cookies=COOKIES, data=DATA)

if response.status_code != 200:
    exit("Error fetching website data")

data = htmlParse(response.text)
data = filterData(data)
print(data)