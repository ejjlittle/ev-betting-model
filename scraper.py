import requests
from bs4 import BeautifulSoup
from constants import URL, HEADERS, COOKIES, DATA

#--PARSE HTML INTO DATA--#
def htmlParse(content):
    soup = BeautifulSoup(content, "html.parser")

    data = [] #list of dicts
    html_table = soup.find("tbody")
    for entry in html_table.find_all("tr"):
        categories = entry.find_all("td")
        bet = {
            "EV": categories[0].text,
            "Sport": categories[4].text,
            "League": categories[5].text,
            "Game": categories[6].text,
            "Market": categories[7].text,
            "BetName": categories[8].text,
            "Odds": categories[9].text,
            "Book": categories[10].text,
            "FairOdds": categories[11].text,
            "BookCount": categories[12].text
        }
        data.append(bet)
    return data

response = requests.post(URL, headers=HEADERS,cookies=COOKIES, data=DATA)

if response.status_code != 200:
    exit("Error fetching website data")

data = htmlParse(response.text)
print(data)


