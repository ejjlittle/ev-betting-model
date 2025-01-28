import requests
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
            "Turnovers": entry[26],
            "Minutes": entry[10]
        }
        playerName = entry[2]
        data[playerName] = statline
    return data


def main(month, day, year):
  #get response from NBA get request
  url = "https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=" + month + "%2F" + day + "%2F" + year + "&DateTo=" + month + "%2F" + day + "%2F" + year + "&Direction=DESC&ISTRound=&LeagueID=00&PlayerOrTeam=P&Season=2024-25&SeasonType=Regular%20Season&Sorter=DATE"
  response = requests.get(url, headers=constants.NBA_HEADERS,)

  #check requests connection
  if response.status_code != 200:
      exit("Error fetching website data")

  data = parseData(response.json())
  return data

if __name__ == "__main__":
    data = main('01', '27', '25') #for testing
    print(data)