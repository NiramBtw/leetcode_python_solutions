class Solution(object):
    def maxProfit(self, prices):

        min_cost = float('inf')
        max_profit = 0
        
        for price in prices:
            min_cost = min(min_cost, price)
            profit = price - min_cost
            max_profit = max(max_profit, profit)
        return max_profit
