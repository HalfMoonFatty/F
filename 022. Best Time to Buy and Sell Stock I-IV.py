'''
Problem 1: Only 1 transaction 

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

import sys
class Solution(object):
    def maxProfit(self, prices):

        minPrice = sys.maxint
        maxprf = 0

        for p in prices:
            minPrice = min(minPrice, p)
            maxprf = max(maxprf, p - minPrice)
        return maxprf
        


'''
Problem 2: As many transactions as possible

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

'''
Do the transic every day
When today's prices is higher than yesterday
If prices keep increase, the result will be the same as buy at first day and sell at last day
'''

class Solution(object):
    def maxProfit(self, prices):

        profit = 0
        for i in range(1, len(prices)):
            profit += max(0,prices[i] - prices[i-1])

        return profit
        
        
        
'''
Problem 3: At most K transactions

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most K transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


import sys
class Solution(object):
    def maxProfit(self, k, prices):

        if len(prices) < 2:
            return 0

        # Greedy part:
        if k > len(prices)/2:
            profit = 0
            for i in range(1,len(prices)):
                profit += max(0,prices[i] - prices[i-1])
            return profit

        # DP part:
        sell = [0 for i in range(k+1)]
        hold = [-sys.maxint+1 for i in range(k+1)]

        for p in prices:
            for i in range(1,k+1):
                sell[i] = max(sell[i], hold[i] + p)
                hold[i] = max(hold[i], sell[i-1] - p)
        return sell[k]
        
        
        

'''
Problem 4: with cooldown + as many transactions as you like 

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:
- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
    prices = [1, 2, 3, 0, 2]
    maxProfit = 3
    transactions = [buy, sell, cooldown, buy, sell]
'''


# Solution : need to make sure when you want to buy a stock, you should base on sell[i-2], to have sell[i-1] as cooldown.

import sys
class Solution(object):
    def maxProfit(self, prices):

        if len(prices)<2:
            return 0

        sell = [0 for i in range(len(prices))]
        hold = [-sys.maxint+1 for i in range(len(prices))]
        hold[0] = -prices[0]

        for i in range(1,len(prices)):
            sell[i] = max(sell[i-1], hold[i-1]+prices[i])
            hold[i] = max(hold[i-1], sell[i-2]-prices[i])
        return sell[-1]
        
