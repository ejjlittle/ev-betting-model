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

    # Iterate over the results to build the stats dictionary
    for dailyData in results:
        date = dailyData["Date"].date()  # Get the date part (year, month, day)
        dailyStats = {
            "Profit": dailyData.get("Profit", 0),
            "AmountWagered": dailyData.get("AmountWagered", 0),
            "NumBets": dailyData.get("NumBets", 0),
            "NumWon": dailyData.get("NumWon", 0),
            "NumLost": dailyData.get("NumLost", 0)
        }

        # Add the stats to the yearlyStats dictionary
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