from pymongo.mongo_client import MongoClient
from datetime import datetime
from decimal import Decimal
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
uri = "mongodb+srv://elittle2:IGnt12YWFH3tYdam@bets-cluster.beqkw.mongodb.net/?retryWrites=true&w=majority&appName=bets-cluster"
client = MongoClient(uri)
db = client["betting-data"]
placedBets = db["placed-bets"]

#do all of this every 5 minutes: updating the website with each new bet placed
now = datetime.now()
dateDay = datetime.strftime(now, "%m/%d/%Y")

dailyData = placedBets.find_one({"Date": dateDay})

#create daily dict if doesn't exist
if not dailyData:
    dailyData = {
        "DailyBets": {},
        "Profit": '0.00',
        "NumBets":0,
        "AmountWagered": '0.00'
    }

#scrape betting data and place accepted bets, updating num bets and amount wagered
cnoData = cnoScraper.main(MINIMUM_EV_PERCENTAGE, MAXIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT)
newBets, amountWagered = model.main(cnoData, UNIT_SIZE, dailyData["DailyBets"], now)
dailyData["NumBets"] += len(newBets)
dailyData["AmountWagered"] = Decimal(dailyData["AmountWagered"]) #convert from str
dailyData["AmountWagered"] += amountWagered

#update the MongoDB
placedBets.update_one(
    {"Date": dateDay}, 
    {
        "$set": {
            "NumBets": dailyData["NumBets"],
            "AmountWagered": str(dailyData["AmountWagered"]), #store as str to preserve precision
            "DailyBets": {**dailyData["DailyBets"], **newBets} #merge new bets into dictionary
        }
    },
    upsert=True #insert if the document doesn't exist
)


#do this at the end of every day (need to make sure this is from yesterday)
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%y")

nbaData = nbaScraper.main(month, day, year)
    
#calculate daily profit and profit per bet
dailyData["DailyBets"], dailyProfit = nbaGrader.main(nbaData, dailyData["DailyBets"])
dailyData["Profit"] = dailyProfit

'''
#update the MongoDB
placedBets.update_one(
        {"date": dateDay}, 
        {
            "$set": {
                "DailyBets": dailyData["DailyBets"],
                "Profit": str(dailyProfit) #store as str to preserve precision
            }
        }
    )
'''
    
print(dateDay, dailyProfit)