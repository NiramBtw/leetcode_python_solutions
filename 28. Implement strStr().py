class Solution(object):
    def strStr(self, haystack, needle):
        """
 ******# return haystack.find(needle) # cuz that func is all ready inside py its super fast 
        
        in python we have in func find() 
        The find() method finds the first occurrence of the specified value.

        The find() method returns -1 if the value is not found.

        The find() method is almost the same as the index() method, the only difference is that           the index() method raises an exception if the value is not found.

        """
        # lets try make a finder
        # haystack = "hello", needle = "ll"
        # so we need to cheak if he == ll , el==ll, ll ==ll , lo == ll
        
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle) + 1):    # the for go on any index to cheak the == , we dont need to cheak the last element 
            if haystack[i : i +len(needle)] == needle:      # we need to cheak 2 elements so i + the len (needle)
                return i
        return -1
            
        
