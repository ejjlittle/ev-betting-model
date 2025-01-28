import json
from shared.db import setup
from gradeBets.nbaGrader import main as calcBets
from gradeBets.nbaScraper import main as scrapeNba
from datetime import datetime

#--GRADE ALL BETS FOR THE CURRENT DATE--#
def gradeBets(placedBets, date):#do this at the end of every day (need to make sure this is from yesterday)
    now = datetime.now()
    date = date or datetime.strftime(now, "%m/%d/%Y")

    dailyData = placedBets.find_one({"Date": date})
    nbaData = scrapeNba(date)
        
    #calculate daily profit and profit per bet
    dailyData["DailyBets"], dailyProfit, numWon, numLost = calcBets(nbaData, dailyData["DailyBets"])

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

def lambdaHandler(event, context):
    placedBets = setup()
    
    #None = default to today
    date = event.get('queryStringParameters', {}).get('date', None)
    gradeBets(placedBets, date)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Bets graded successfully'})
    }

if __name__ == "__main__":
    placedBets = setup()
    gradeBets(placedBets, None)
