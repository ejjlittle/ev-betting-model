import json
from decimal import Decimal
from shared.constants import MINIMUM_EV_PERCENTAGE, MAXIMUM_EV_PERCENTAGE, LEAGUES, BOOKS, MINIMUM_BOOK_COUNT, UNIT_SIZE
from shared.db import setup
from datetime import datetime
import placeBets.cnoScraper as cnoScraper
import placeBets.model as model
import pytz

#--PLACE BETS BASED ON MODEL AND UPDATE DB--#
def placeBets(placedBets):
    now = datetime.now(pytz.timezone('US/Eastern'))
    date = now.replace(hour=0, minute=0, second=0, microsecond=0)

    placedBets = setup()
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

    #scrape betting data and place accepted bets, updating db
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
    return newBets

#--RUN EVERY MINUTE VIA CLOUDWATCH ON AWS LAMBDA--#
def lambdaHandler(event, context):
    placedBets = setup()
    placeBets(placedBets)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Bets placed successfully'})
    }


if __name__ == "__main__":
    placedBets = setup()
    newBets = placeBets(placedBets)
    print(newBets) #for dev