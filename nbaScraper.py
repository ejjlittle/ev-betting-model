import requests
from bs4 import BeautifulSoup
import constants

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
            "Turnovers": entry[26]
        }
        playerName = entry[2]
        data[playerName] = statline
    return data

def main():
  #get response from NBA get request
  response = requests.get(constants.NBA_URL, 
                          headers=constants.NBA_HEADERS,
                          cookies=constants.NBA_COOKIES,
                            params=constants.NBA_PARAMS)

  #check requests connection
  if response.status_code != 200:
      exit("Error fetching website data")

  data = parseData(response.json())
  return data

if __name__ == "__main__":
    data = main() #for testing
    print(data)