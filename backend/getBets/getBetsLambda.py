import json
from shared.db import setup
from datetime import datetime
import pytz

#--ENDPOINT FOR DAILY DATA--#
def lambdaHandler(event, context):
    placedBets = setup()
    
    date = event.get('queryStringParameters', {}).get('date', None)
    #try to convert date into a datetime object
    try:
        date = datetime.strptime(date, "%Y-%m-%d") #YYYY-MM-DD
        est = pytz.timezone('US/Eastern')
        date = est.localize(date) #convert to est
    except (TypeError, ValueError, AttributeError) as e:
        return {
            'statusCode': 400, #bad request
            'body': json.dumps({'message': 'Invalid date format (YYYY-MM-DD)'})
        }
        
    dailyData = placedBets.find_one({"Date": date})
    if not dailyData:
        return {
            'statusCode': 404,  #not found
            'body': json.dumps({'message': 'No bets found for this date'})
        }
    return {
        'statusCode': 200,
        'body': json.dumps(placedBets.find_one({"Date": date})["DailyBets"])
    }