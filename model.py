import pytz
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

#--GENERAL CONSTANTS--#
EST = pytz.timezone("US/Eastern")
FORMAT = "%m/%d/%Y %H:%M:%S"

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

#--FORMAT TIME TO EST--#
def formatTime(time):
    t = datetime.strptime(time, "%m/%d/%Y %I:%M:%S %p")
    t = pytz.utc.localize(t)
    estTime = t.astimezone(EST)
    return estTime

def main(data, unitSize, dailyBets, time):
    for entry in data:
        date = formatTime(entry["Date"])
        #only place bets within the same day
        if not (date.year == time.year and date.month == time.month and date.day == time.day):
            continue

        #only player props
        if entry["Market"].split()[0] != "Player":
            continue

        #only quantifiable lines
        if not (entry["BetName"].split()[-2] == "Over" or entry["BetName"].split()[-2] == "Under"):
            continue

        #no lines with too much correlation
        player = ' '.join(entry["BetName"].split()[:-2])
        if player in dailyBets:
            continue

        #bet is good - format data
        bet = {
            "Wager": Decimal(qKelly(entry["FairOdds"], entry["Odds"]) * 100 * unitSize).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) , #amount bet
            "Profit": Decimal(0).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP), #profit is 0.00 until graded
            "EV": entry["EV"], #expected value as percentage
            "Date": datetime.strftime(date, "%m/%d/%Y"), #eg. 1/25/2025
            "GameTime": datetime.strftime(date, "%I:%M %p"), #eg. 7:30 pm
            "TimePlaced": datetime.strftime(time, "%I:%M %p"), #eg. 1:46 pm
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
        dailyBets[player] = bet
    
    return dailyBets