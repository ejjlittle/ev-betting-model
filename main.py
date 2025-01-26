import pytz
from datetime import datetime
import cnoScraper
import nbaScraper

#--BETTING MODEL CONSTANTS--#
MINIMUM_EV_PERCENTAGE = 7
MAXIMUM_EV_PERCENTAGE = 40
LEAGUES = ["NBA"]
BOOKS = ["FanDuel", "DraftKings", "BetMGM"]
MINIMUM_BOOK_COUNT = 5

#--GENERAL CONSTANTS--#
EST = pytz.timezone("US/Eastern")
FORMAT = "%m/%d/%Y %H:%M:%S"

#--FORMAT TIME TO EST--#
def formatTime(time):
    t = datetime.strptime(time, "%m/%d/%Y %I:%M:%S %p")
    t = pytz.utc.localize(t)
    estTime = t.astimezone(EST)
    return estTime

#--CHECK IF A STRING CAN BE TURNED TO FLOAT--#
def isFloat(string):
  for char in string:
    if not (char.isnumeric() or char == '.'):
      return False
  return True

bets = [] #list of bets that the model takes

cnoData = cnoScraper.main(MINIMUM_EV_PERCENTAGE, MAXIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT)
now = datetime.now()
for entry in cnoData:
    date = formatTime(entry["Date"])
    #only place bets within the same day
    if not (date.year == now.year and date.month == now.month and date.day == now.day):
        continue
    #only player props
    if entry["Market"].split()[0] != "Player":
        continue
    #only quantifiable lines
    if isFloat(entry["BetName"].split()[-1]):
       continue
    #no lines with too much correlation
    