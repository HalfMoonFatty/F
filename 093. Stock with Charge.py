'''
Problem:

Can finish as many transactions as you want. Each transaction has a charge. What is the max profit you can get?

'''

def maxProfitWithCharge(prices, charge):
    profit = 0
    localProfit = 0
    charged = False
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            localProfit += prices[i] - prices[i-1]
            if charged:
                localProfit -= charge
            charged = True
        elif charged:
            profit += localProfit if localProfit > 0 else 0
            localProfit = 0
            charged = False
    if localProfit > 0:
        profit += localProfit

    return profit
