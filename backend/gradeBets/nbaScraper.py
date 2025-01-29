import requests
import shared.constants as constants
from dotenv import load_dotenv
import os

#--UNPACK RAW DATA TO DICTIONARY--#
def parseData(content):
    data = {}
    raw = content["resultSets"][0]["rowSet"]
    for entry in raw:
        statline = {
            "Points": entry[28],
            "Rebounds": entry[22],
            "Assists": entry[23],
            "Threes": entry[14],
            "Steals": entry[24],
            "Blocks": entry[25],
            "Turnovers": entry[26],
            "Minutes": entry[10]
        }
        playerName = entry[2]
        data[playerName] = statline
    return data


def main(date):
    #load proxies (unnecessary on local device)
    '''
    load_dotenv(dotenv_path='../.env')

    proxies = {
        "http": os.getenv("PROXY_HTTP"),
        "https": os.getenv("PROXY_HTTPS")
    }
    '''

    #get response from NBA get request
    date = date.split('/')
    url = "https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=" + date[0] + "%2F" + date[1] + "%2F" + date[2][-2:] + "&DateTo=" + date[0] + "%2F" + date[1] + "%2F" + date[2][-2:] + "&Direction=DESC&ISTRound=&LeagueID=00&PlayerOrTeam=P&Season=2024-25&SeasonType=Regular%20Season&Sorter=DATE"
    response = requests.get(url, headers=constants.NBA_HEADERS)

    #check requests connection
    if response.status_code != 200:
        exit("Error fetching website data")

    data = parseData(response.json())
    return data


if __name__ == "__main__":
    data = main("1/29/25") 
    print(data) #for dev