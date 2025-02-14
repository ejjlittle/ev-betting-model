import json
from shared.db import setup
from datetime import datetime, timedelta
from pprint import pprint

#--GET DAILY STATS FOR LAST 365 DAYS--#
def getStats(placedBets):
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    startDate = today - timedelta(days=366)
    
    #query MongoDB for all records in the last 365 days
    results = placedBets.find({
        "Date": {
            "$gte": startDate,
            "$lt": today #exclude today
        }
    })
    
    yearlyStats = {}

    #build the stats dictionary
    for dailyData in results:
        date = dailyData["Date"]
        dailyStats = {
            "Profit": dailyData.get("Profit", 0),
            "AmountWagered": dailyData.get("AmountWagered", 0),
            "NumBets": dailyData.get("NumBets", 0),
            "NumWon": dailyData.get("NumWon", 0),
            "NumLost": dailyData.get("NumLost", 0)
        }

        yearlyStats[str(date)] = dailyStats

    return yearlyStats

#--ENDPOINT FOR ALL STATS NEEDED TO LOAD WEBPAGE--#
def lambdaHandler(event, context):
    placedBets = setup()
    
    return {
        'statusCode': 200,
        'body': json.dumps(getStats(placedBets))
    }


if __name__ == "__main__":
    placedBets = setup()
    pprint(getStats(placedBets)) #for dev