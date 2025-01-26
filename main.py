import requests
from bs4 import BeautifulSoup
import CNO_Constants

#--BETTING MODEL CONSTANTS--#
MINIMUM_EV_PERCENTAGE = 7
MAXIMUM_EV_PERCENTAGE = 40
LEAGUES = ["NBA"]
BOOKS = ["FanDuel", "DraftKings", "BetMGM"]
MINIMUM_BOOK_COUNT = 5

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
    for i in range(len(data)): #filter by min EV
        if data[i]["EV"] < MINIMUM_EV_PERCENTAGE:
            data = data[:i]
            break
    for i in range(len(data)): #filter by max EV
        if data[i]["EV"] < MINIMUM_EV_PERCENTAGE:
            data = data[:i]
            break
    data = [entry for entry in data if entry["League"] in LEAGUES] #filter by league
    data = [entry for entry in data if entry["Book"] in BOOKS] #filter by book
    data = [entry for entry in data if entry["BookCount"] >= MINIMUM_BOOK_COUNT] #filter by book count
    return data

#get html response from CNO post request
response = requests.post(CNO_Constants.URL, 
                         headers=CNO_Constants.HEADERS,
                         cookies=CNO_Constants.COOKIES,
                           data=CNO_Constants.DATA)

#check requests connection
if response.status_code != 200:
    exit("Error fetching website data")

cnoData = htmlParse(response.text)
cnoData = filterData(cnoData)
print(cnoData)