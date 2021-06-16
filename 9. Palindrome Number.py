class Solution:
    def isPalindrome(self, x):
        """
        cheak if the num is a Palindrome 
        121 filped  121 -> true ....
        123 fliped 321 -> false ....
        Palindrome cant be a neg number 
        
        1. create copy and flip if == true 
        so its a Palindrome 
         think case :
         
         x = 1215 # input
         c = 1215 # making a copy
         b = 0 # backwards
         1215 % 10 = 5
         1215 /10 = 121 # we have int only so no 0.000
         now 
         c =121
         b = 0 * 10 + 4 -> 4
         # 1 more time 
         121 % 10
         121 / 10
         c = 12
         b = 4 *10 + 1 -> 41
         
         b = 4121 
         now comper x == b if true its a Palindrome
         else not 
         
       
        # firts lets look if its a neg int - we cant hold neg 
        
        if x < 0:
            return False
        
        c = x # copy 121
        b = 0 # backwards
         
        while c:
            b = b * 10 + c % 10
            c //= 10
            
        return b == x
         """
        # trying to work with list hold and just comper as str 

        val = str(x) # making the int ->str 
        val2 = val[::-1] # desc the order 
        return val == (val2)
 

















