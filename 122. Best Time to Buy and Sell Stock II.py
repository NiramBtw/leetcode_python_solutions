class Solution(object):
    def maxProfit(self, price):
        # hold 1 obj to hold the count
        profit = 0
        # and using 1 pointer to know where r we 
        for i in range(1, len(price)): # skip [0] cuz we comper 
            # to the last val
            if price[i] > price[i-1]:
                profit += (price[i] - price[i-1])
        return profit
    
            

        
        
