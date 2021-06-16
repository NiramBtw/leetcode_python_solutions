class Solution(object):
    def removeElement(self, nums, val):
        """
        * dont care about order.
        * cant create new array to help 
        * need to modifiy the input
        
        
       
        i = 0 
        last = len(nums) - 1
        while i <= last:
            if nums[i] == val:
                nums[i] = nums[last]
                nums[last] = nums[i]
                last -= 1
            else:
                i += 1
        return last + 1
         """
        
        while(val in nums):
            nums.remove(val)
        return len(nums)
