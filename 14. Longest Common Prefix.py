class Solution:
    def longestCommonPrefix(self, strs):
        """
        * first we know all words r in low case - so saving time now use strs.lower()
        1. then look if its an srt ?
        2. shorting val via the len(strs)
        if all(strs) -will cheak in one any vals in strs 
        using startswith() to find common prefix
        """
        long_pre = ''
        if not strs:
            return long_pre
        shorting = min(strs, key=len)
        for i in range(len(shorting)):
            if all([x.startswith(shorting[:i+1]) for x in strs]):
                long_pre = shorting[:i+1]
            else:
                break
        return long_pre
        
        
        
        
