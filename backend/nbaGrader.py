from decimal import Decimal
from constants import PLAYER_NAMES

TWOPLACES = Decimal(10) ** -2

#--AMERICAN ODDS TO DECIMAL ODDS--#
def americanDecimal(odds):
    if odds[0] == '+':
        odds = int(odds[1:]) / 100
    else:
        odds = 100 / int(odds[1:])
    return odds

#--GET THE PLAYER STATLINE BASED ON BET NAME--#
def getStatline(player, market, data):
    if not player in data:
        return
    
    total = Decimal(0)
    marketStr = market.split()[1:] #exclude "Player"
    stats = []
    for i in range(len(marketStr)):
        if i % 2 == 0: #only even indexes have stats
            stats.append(marketStr[i])
    
    for stat in stats:
        total += data[player][stat]

    return total


def main(data, dailyBets):
    dailyProfit = 0
    numWon = 0
    numLost = 0
    for player, bet in dailyBets.items():
        statline = getStatline(player, bet["Market"], data)

        if not statline and player in PLAYER_NAMES: #try again with alternative name
            altPlayer = PLAYER_NAMES[player]
            statline = getStatline(altPlayer, bet["Market"], data)
            if not statline or data[altPlayer]["Minutes"] == 0: #no data or player did not play (bet voided)
                continue
        elif not statline or data[player]["Minutes"] == 0: #no data or player did not play (bet voided)
            continue
            
        line = float(bet["BetName"].split()[1])
        if bet["BetName"].split()[0] == "Over" and statline > line: #bet won
            profit = Decimal(bet["Wager"]) * Decimal(str(americanDecimal(bet["Odds"]))) 
            numWon += 1
        elif bet["BetName"].split()[0] == "Under" and statline < line: #bet won
            profit = Decimal(bet["Wager"]) * Decimal(str(americanDecimal(bet["Odds"])))
            numWon += 1
        else: #bet lost
            profit = Decimal(bet["Wager"]) * -1
            numLost += 1
        bet["Profit"] = profit.quantize(TWOPLACES)
        dailyProfit += bet["Profit"]
        bet["Profit"] = str(bet["Profit"]) #store as str to preserve precision
        print(player, bet["Profit"])

    return dailyBets, dailyProfit, numWon, numLost