class Solution:
    def reverse(self, x):
        """
        say we have input -> 123 we need to give back -> 321
        to get the 3 out of 123 we can use mod %
        
        123 % 10 -> 3
        123 / 12 -> 12
        
        12 % 10 -> 2
        12 / 10 ->1
        
        3*10 ->30
        30+2 -> 32
        i that case we need to consider [-231, 231 - 1]
        
        im thinking using while loop to iterat 
        
        now we can look on the genral case of -2**31 to 2**31 thats it the pop
        
        """
        # cus py is having a pro when -123/10 -gives -13 
        # cuz -12.3int going to -13 ;
        # so mb rap it up with a func to fix it 
        
        def divide(number, divider):
            return int(number * 1.0 / divider)
        def mod(number, m):
            if number < 0:
                return number % -m
            return number % m
        
        max_int = 2**31 -1 
        min_int = -2**31
        res = 0
        while x:
            pop = mod(x,10) # get the first dig
            x = divide(x,10) # get the rest x= -10
            # to chack if in the popultion numbers
            if res > divide(max_int, 10) or (res == divide(max_int, 10) and pop > 7):
                return 0
            if res < divide(min_int, 10) or (res == divide(min_int, 10) and pop < -8):
                return 0            
            res = res *10 + pop
            
        return res
        """
        Input:
1534236469
Output:
9646324351
?
need to lim if > maxint  or <minint 
        """
