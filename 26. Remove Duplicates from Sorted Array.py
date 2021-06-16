class Solution(object):
    def removeDuplicates(self, nums):
        """
        nums= [1,1,2,2,3,4]
        create and index of all unique chars in the list 
        then remove all the rest 
        return the new index list we make 
        + the len of them 
        
        """
        # first cond
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        j = 0   # index count
        
        for i in range(1,len(nums)):    # loop any element in nums 
            if nums[i] != nums[j]:  # if number index i is diff the j
                j += 1  # add 1 to the count
                nums[j] = nums[i]
        return j + 1 # because we start look from 0
            
        
