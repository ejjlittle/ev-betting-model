import json
from shared.db import setup
from datetime import datetime, timedelta
from pprint import pprint

#--GET DAILY STATS FOR LAST 365 DAYS--#
def getStats(placedBets):
    today = datetime.today()
    startDate = today - timedelta(days=365)
    yearlyStats = {}

    yearlyDays = [today - timedelta(days=i) for i in range(1, 366)] #exclude today
    yearlyStats = {}

    for dateObj in yearlyDays:
        date = datetime.strftime(dateObj, "%m/%d/%Y")
        dailyData = placedBets.find_one({"Date": date})

        if not dailyData: #account for days before data collection
            continue

        dailyStats = {
            "Profit": dailyData.get("Profit", 0),
            "AmountWagered": dailyData.get("AmountWagered", 0),
            "NumBets": dailyData.get("NumBets", 0),
            "NumWon": dailyData.get("NumWon", 0),
            "NumLost": dailyData.get("NumLost", 0)
        }

        yearlyStats[date] = dailyStats

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