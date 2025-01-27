from decimal import Decimal
from datetime import datetime
import model
import nbaGrader
import cnoScraper
import nbaScraper

#--BETTING MODEL CONSTANTS--#
MINIMUM_EV_PERCENTAGE = 0
MAXIMUM_EV_PERCENTAGE = 40
LEAGUES = ["NBA"]
BOOKS = ["FanDuel", "DraftKings", "BetMGM"]
MINIMUM_BOOK_COUNT = 5
UNIT_SIZE = 50

totalProfit = 0
placedBets = {'01/26/2025': {'DailyBets': {'Shai Gilgeous-Alexander': {'Wager': Decimal('39.31'), 'Profit': Decimal('0.00'), 'EV': 3.59, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Turnovers', 'BetName': 'Under 2.5', 'Odds': '+120', 'Book': 'BetMGM', 'FairOdds': '+112', 'BookCount': 5}, 'Aaron Wiggins': {'Wager': Decimal('24.51'), 'Profit': Decimal('0.00'), 'EV': 2.0, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Points', 'BetName': 'Under 11.5', 'Odds': '+100', 'Book': 'FanDuel', 'FairOdds': '-104', 'BookCount': 12}, 'Isaiah Hartenstein': {'Wager': Decimal('22.07'), 'Profit': Decimal('0.00'), 'EV': 1.82, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Assists', 'BetName': 'Over 3.5', 'Odds': '+110', 'Book': 'FanDuel', 'FairOdds': '+106', 'BookCount': 12}, 'Jalen Williams': {'Wager': Decimal('11.73'), 'Profit': Decimal('0.00'), 'EV': 0.82, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Blocks + Steals', 'BetName': 'Over 2.5', 'Odds': '+105', 'Book': 'DraftKings', 'FairOdds': '+103', 'BookCount': 5}, 'Donovan Clingan': {'Wager': Decimal('0.00'), 'Profit': Decimal('0.00'), 'EV': 0.1, 'Date': '01/26/2025', 'GameTime': '06:02 PM', 'TimePlaced': '05:57 PM', 'Sport': 'Basketball', 'League': 'NBA', 'Game': 'Oklahoma City Thunder @ Portland Trail Blazers', 'Market': 'Player Blocks', 'BetName': 'Over 1.5', 'Odds': '-140', 'Book': 'FanDuel', 'FairOdds': '-140', 'BookCount': 8}}, 'Profit': 0}} #{date: {"DailyBets": {player: {bet}}, "Profit": 50}}

#do all of this every 5 minutes: updating the website with each new bet placed
now = datetime.now()
dateDay = datetime.strftime(now, "%m/%d/%Y")

#create daily dict
if not dateDay in placedBets:
    placedBets[dateDay] = {
        "DailyBets": {},
        "Profit": 0
    }

cnoData = cnoScraper.main(MINIMUM_EV_PERCENTAGE, MAXIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT)
placedBets[dateDay]["DailyBets"] = model.main(cnoData, UNIT_SIZE, placedBets[dateDay]["DailyBets"], now)

#do this at the end of every day (need to make sure this is from yesterday)
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%Y")
nbaData = nbaScraper.main(month, day, year)
    
#store daily profit
placedBets[dateDay]["DailyBets"], dailyProfit = nbaGrader.main(nbaData, placedBets[dateDay]["DailyBets"])
placedBets[dateDay]["Profit"] = dailyProfit