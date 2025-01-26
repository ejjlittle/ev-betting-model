import pytz
from datetime import datetime
import cnoScraper
import nbaScraper

#--BETTING MODEL CONSTANTS--#
MINIMUM_EV_PERCENTAGE = 0
MAXIMUM_EV_PERCENTAGE = 40
LEAGUES = ["NBA", "NFL"]
BOOKS = ["FanDuel", "DraftKings", "BetMGM"]
MINIMUM_BOOK_COUNT = 5
UNIT_SIZE = 50

#--GENERAL CONSTANTS--#
EST = pytz.timezone("US/Eastern")
FORMAT = "%m/%d/%Y %H:%M:%S"


#--FORMAT TIME TO EST--#
def formatTime(time):
    t = datetime.strptime(time, "%m/%d/%Y %I:%M:%S %p")
    t = pytz.utc.localize(t)
    estTime = t.astimezone(EST)
    return estTime

#--GET THE PLAYER STATLINE BASED ON BET NAME--#
def getStatline(player, market, data):
    if not data[player]:
        return
    
    total = 0
    marketStr = market.split()[1:] #exclude "Player"
    stats = []
    for i in range(len(marketStr)):
        if i % 2 == 0: #only even indexes have stats
            stats.append(marketStr[i])
    
    for stat in stats:
        total += data[player][stat]
    return total

#--GET PERCENTAGE OF WINNING FROM FAIR ODDS--#
def fairOddsPercentage(fairOdds):
    if fairOdds[0] == '+':
        fairOdds = int(fairOdds[1:])
        percent = 100 / (fairOdds + 100)
    else:
        fairOdds = int(fairOdds[1:])
        percent = fairOdds / (fairOdds + 100)
    return percent

#--AMERICAN ODDS TO DECIMAL ODDS--#
def americanDecimal(odds):
    if odds[0] == '+':
        odds = int(odds[1:]) / 100
    else:
        odds = 100 / int(odds[1:])
    return odds

#--KELLY CRITERION CALCULATOR--#
def kelly(fairOdds, odds):
    b = americanDecimal(odds)
    p = fairOddsPercentage(fairOdds)
    f = p - (1- p) / b
    return f


placedBets = {} #{date: {player: {bet}}}

#do all of this every 5 minutes: updating the website with each new bet placed
cnoData = cnoScraper.main(MINIMUM_EV_PERCENTAGE, MAXIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT)
now = datetime.now()
dateDay = datetime.strftime(now, "%m/%d/%Y")
if not dateDay in placedBets:
    placedBets[dateDay] = {}

for entry in cnoData:
    date = formatTime(entry["Date"])
    #only place bets within the same day
    if not (date.year == now.year and date.month == now.month and date.day == now.day):
        continue

    #only player props
    if entry["Market"].split()[0] != "Player":
        continue

    #only quantifiable lines
    if not (entry["BetName"].split()[-2] == "Over" or entry["BetName"].split()[-2] == "Under"):
       continue

    #no lines with too much correlation
    player = ' '.join(entry["BetName"].split()[:-2])
    if player in placedBets[dateDay]:
        continue

    #bet is good - format data
    bet = {
        "Wager": kelly(entry["FairOdds"], entry["Odds"]) * 1000 * UNIT_SIZE, #eg. 76
        "EV": entry["EV"], #expected value as percentage
        "Date": datetime.strftime(date, "%m/%d/%Y"), #eg. 1/25/25
        "GameTime": datetime.strftime(date, "%I:%M %p"), #eg. 7:30 pm
        "TimePlaced": datetime.strftime(now, "%I:%M %p"), #eg. 1:46 pm
        "Sport": entry["Sport"], #eg. Basketball
        "League": entry["League"], #eg. NBA
        "Game": entry["Game"], #eg. Milwaukee Bucks @ Golden State Warriors
        "Market": entry["Market"], #eg. Player Threes
        "BetName": ' '.join(entry["BetName"].split()[-2:]), #eg. Over 2.5
        "Odds": entry["Odds"], #eg. -170
        "Book": entry["Book"], #eg. DraftKings
        "FairOdds": entry["FairOdds"], #eg. -200
        "BookCount": entry["BookCount"] #number of books where bet is available
    }
    #place the bet
    placedBets[dateDay][player] = bet

#do this at the end of every day (need to make sure this is from yesterday)
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%y")

nbaData = nbaScraper.main(month, day, year)
for player, bet in placedBets['/'.join(month, day, year)].items():
    statline = getStatline(player, bet["Market"], nbaData)

