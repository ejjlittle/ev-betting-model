import pytz
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
import cnoScraper
import nbaScraper

#--BETTING MODEL CONSTANTS--#
MINIMUM_EV_PERCENTAGE = 0
MAXIMUM_EV_PERCENTAGE = 40
LEAGUES = ["NBA"]
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
    if not player in data or data[player]["Minutes"] == 0:
        return
    
    total = Decimal(0)
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

#--QUARTER KELLY CRITERION CALCULATOR--#
def qKelly(fairOdds, odds):
    b = americanDecimal(odds)
    p = fairOddsPercentage(fairOdds)
    f = p - (1- p) / b
    return f * 0.25

totalProfit = 0
placedBets = {'01/26/2025': {'DailyBets': {'Shai Gilgeous-Alexander': {'Wager': Decimal('39.31'), 'Profit': Decimal('0.00'), 'EV': 3.59, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Turnovers', 'BetName': 'Under 2.5', 'Odds': '+120', 'Book': 'BetMGM', 'FairOdds': '+112', 'BookCount': 5}, 'Aaron Wiggins': {'Wager': Decimal('24.51'), 'Profit': Decimal('0.00'), 'EV': 2.0, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Points', 'BetName': 'Under 11.5', 'Odds': '+100', 'Book': 'FanDuel', 'FairOdds': '-104', 'BookCount': 12}, 'Isaiah Hartenstein': {'Wager': Decimal('22.07'), 'Profit': Decimal('0.00'), 'EV': 1.82, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Assists', 'BetName': 'Over 3.5', 'Odds': '+110', 'Book': 'FanDuel', 'FairOdds': '+106', 'BookCount': 12}, 'Jalen Williams': {'Wager': Decimal('11.73'), 'Profit': Decimal('0.00'), 'EV': 0.82, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Blocks + Steals', 'BetName': 'Over 2.5', 'Odds': '+105', 'Book': 'DraftKings', 'FairOdds': '+103', 'BookCount': 5}, 'Donovan Clingan': {'Wager': Decimal('0.00'), 'Profit': Decimal('0.00'), 'EV': 0.1, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Blocks', 'BetName': 'Over 1.5', 'Odds': '-140', 'Book': 'FanDuel', 'FairOdds': '-140', 'BookCount': 8}}, 'Profit': 0}} #{date: {"DailyBets": {player: {bet}}, "Profit": 50}}

#do all of this every 5 minutes: updating the website with each new bet placed
cnoData = cnoScraper.main(MINIMUM_EV_PERCENTAGE, MAXIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT)
now = datetime.now()
dateDay = datetime.strftime(now, "%m/%d/%Y")
#create daily dict
if not dateDay in placedBets:
    placedBets[dateDay] = {
        "DailyBets": {},
        "Profit": 0
    }

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
    if player in placedBets[dateDay]["DailyBets"]:
        continue

    #bet is good - format data
    bet = {
        "Wager": Decimal(qKelly(entry["FairOdds"], entry["Odds"]) * 100 * UNIT_SIZE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) , #amount bet
        "Profit": Decimal(0).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), #profit is 0.00 until graded
        "EV": entry["EV"], #expected value as percentage
        "Date": datetime.strftime(date, "%m/%d/%Y"), #eg. 1/25/2025
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
    placedBets[dateDay]["DailyBets"][player] = bet

#do this at the end of every day (need to make sure this is from yesterday)
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%Y")
dateDay = '/'.join([month, day, year])
nbaData = nbaScraper.main(month, day, year)
dailyProfit = 0
for player, bet in placedBets[dateDay]["DailyBets"].items():
    statline = getStatline(player, bet["Market"], nbaData)
    if not statline: #no data or player did not play (bet voided)
        continue

    line = int(bet["BetName"].split()[1])
    if bet["BetName"].split()[0] == "Over" and statline > line: #bet won
        profit = Decimal(bet["Wager"] * americanDecimal(bet["Odds"])) 
    elif bet["BetName"].split()[0] == "Under" and statline <= line: #bet won
        profit = Decimal(bet["Wager"] * americanDecimal(bet["Odds"]))
    else: #bet lost
        profit = -bet["Wager"]
    bet["Profit"] = profit.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    dailyProfit += profit
    print(player, profit)

#store daily profit
placedBets[dateDay]["Profit"] = dailyProfit
print(dateDay, dailyProfit)
    
