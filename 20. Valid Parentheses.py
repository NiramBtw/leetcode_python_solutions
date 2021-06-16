class Solution:
    def isValid(self, s):
        """
        rules:
        1. need to id the type of the brackets
        2. then count the total types across the str
        3. look at the order .
        lats in first out?
        
        making a holder that go for some ifs and elifs to valid the str 
        
        """
        if not s or len(s) == 0:
            return True
        
        holder = []     # here storing the valids
        
        for char in s:  # diff the chars that valid for us 
            if char == '(' or char == '[' or char == '{':
                #if they push to the holder 
                holder.append(char)
            # now cheak if ) is not the first and ( is not the last 
            # if 1 of the cond here so the str not valid
            elif char == ')' and (len(holder) == 0 or holder[-1] != '(' ):
                return False
            # the rep for all kind of brackets
            elif char == ']' and (len(holder) == 0 or holder[-1] != '[' ):
                return False
            elif char == '}' and (len(holder) == 0 or holder[-1] != '{' ):
                return False
            # if non match so last element need to be remove for holder 
            else:
                holder.pop()
        
        # need to cheak if holder is empty 
        # cuz if we have any in holder ist mean we have more open\ close brackets 
        # then need to be 
        if len(holder) > 0:
            return False
        
        return True
                
            
                
            
