import json
from shared.db import setup
from gradeBets.nbaGrader import main as calcBets
from gradeBets.nbaScraper import main as scrapeNba
from datetime import datetime, timedelta
import pytz

#--GRADE ALL BETS FOR THE CURRENT DATE--#
def gradeBets(placedBets, date):
    now = datetime.now()
    est = pytz.timezone('US/Eastern')
    estNow = now.astimezone(est)
    previousDay = estNow - timedelta(days=1)
    date = date or datetime.strftime(previousDay, "%m/%d/%Y")

    dailyData = placedBets.find_one({"Date": date})
    nbaData = scrapeNba(date)
        
    #calculate daily profit and profit per bet
    dailyData["DailyBets"], dailyProfit, numWon, numLost = calcBets(nbaData, dailyData["DailyBets"])

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
    
    return date, dailyProfit, numWon, numLost

#--RUN 5AM EST EVERYDAY VIA CLOUDWATCH ON AWS LAMBDA--#
def lambdaHandler(event, context):
    placedBets = setup()
    
    #None = default to yesterday
    date = event.get('queryStringParameters', {}).get('date', None)
    gradeBets(placedBets, date)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Bets graded successfully'})
    }


if __name__ == "__main__":
    placedBets = setup()
    date, dailyProfit, numWon, numLost = gradeBets(placedBets, "01/29/2025")
    print(date, dailyProfit, numWon, numLost) #for dev
