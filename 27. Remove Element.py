class Solution(object):
    def removeElement(self, nums, val):
        """
        * dont care about order.
        * cant create new array to help 
        * need to modifiy the input
        * if we look at that like a index map so we dont care how many time any char is in the list
        * we only care about the unique so as long as the val pop 1s we can pin it and remove the 
        *rest
        ******************
        first try
        ***************
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
        # sec try more simple way
        
        while(val in nums):
            nums.remove(val)
        return len(nums)
