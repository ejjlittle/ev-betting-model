from pymongo.mongo_client import MongoClient
from datetime import datetime
from decimal import Decimal
from dotenv import load_dotenv
import os
import model
import nbaGrader
import cnoScraper
import nbaScraper

#--BETTING MODEL CONSTANTS--#
MINIMUM_EV_PERCENTAGE = 7
MAXIMUM_EV_PERCENTAGE = 40
LEAGUES = ["NBA"]
BOOKS = ["FanDuel", "DraftKings", "BetMGM"]
MINIMUM_BOOK_COUNT = 5
UNIT_SIZE = 50

#--MONGO DB--#
load_dotenv()
uri = os.environ.get("MONGO_URI")
client = MongoClient(uri)
db = client["betting-data"]
placedBets = db["placed-bets"]

#do all of this every 5 minutes: updating the website with each new bet placed
now = datetime.now()
date = datetime.strftime(now, "%m/%d/%Y")

dailyData = placedBets.find_one({"Date": date})

#create daily dict if doesn't exist
if not dailyData:
    dailyData = {
        "DailyBets": {},
        "Profit": '0',
        "AmountWagered": '0',
        "NumBets": 0,
        "NumWon": 0,
        "NumLost": 0
    }

#scrape betting data and place accepted bets, updating num bets and amount wagered
cnoData = cnoScraper.main(MINIMUM_EV_PERCENTAGE, MAXIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT)
newBets, amountWagered = model.main(cnoData, UNIT_SIZE, dailyData["DailyBets"], now)
dailyData["NumBets"] += len(newBets)
dailyData["AmountWagered"] = Decimal(dailyData["AmountWagered"]) #convert from str
dailyData["AmountWagered"] += amountWagered

#update the MongoDB
placedBets.update_one(
    {"Date": date}, 
    {
        "$set": {
            "DailyBets": {**dailyData["DailyBets"], **newBets}, #merge new bets into dictionary
            "AmountWagered": str(dailyData["AmountWagered"]), #store as str to preserve precision
            "Profit": dailyData["Profit"],
            "NumBets": dailyData["NumBets"],
            "NumWon": dailyData["NumWon"],
            "NumLost": dailyData["NumLost"]
        }
    },
    upsert=True #insert if the document doesn't exist
)


#do this at the end of every day (need to make sure this is from yesterday)
nbaData = nbaScraper.main(date)
    
#calculate daily profit and profit per bet
dailyData["DailyBets"], dailyProfit, numWon, numLost = nbaGrader.main(nbaData, dailyData["DailyBets"])

'''
placedBets.update_many(
    {"Date": date},
    {
        "$set": {
            "DailyBets": dailyData["DailyBets"],
            "Profit": str(dailyProfit),  #store as str to preserve precision
            "NumWon": numWon,
            "NumLost": numLost
        }
    }
)
'''
    
print(date, dailyProfit)