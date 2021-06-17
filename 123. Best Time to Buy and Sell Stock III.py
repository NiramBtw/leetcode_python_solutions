class Solution(object):
    def maxProfit(self, prices):
        """
        prices = [3,3,5,0,0,3,1,4]
        state - rest, hold, sell
        * can to only 2 transactions
        start at 0 no stock
        the stock price is postive 
        """
        
        # states
        a = -prices[0] # -3 take a negative val because its a buy 
        b = float('-inf') # -inf
        c = float('-inf') # -inf
        d = float('-inf') # -inf
        
        for price in prices:  # price- 3
            a = max(a, -price)  # buy 
            b = max(b, a + price)   # sell
            c = max(c, b -price)    # buy 
            d = max(d, c + price)   # sell and last state
        return d
