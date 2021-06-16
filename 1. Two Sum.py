class Solution:
    
    def twoSum(self,nums,target):
        # by try give 1 num vs the target we can cheack if the num(we look) 
        # + the num we hold  = traget 
        # nums = [2,7,11,15], target = 9
        # try use a dict()
        comp_map = dict()
        
        for i in range(len(nums)):
            num = nums[i] # 7?
            comp = target - nums[i]# comp = 2
            
            if num in comp_map: # here we r find the pair 
                return [comp_map[num], i]
            else:
                comp_map[comp] = i # {7,0}
                                
"""          
        
    # he i use 2 for loops which make its run long time     
    def naive_twoSum(self, nums, target):
        
        for i in range(len(nums)): # run all elements in nums
            for j in range(i+1, len(nums)): # loop for the sec nums no run same elemet 
                #2 time i+1
                sum = nums[i] + nums[j] #same as traget
                if sum == target:
                    return [i,j]
"""
                
if __name__ == '__main__':

    s = Solution()
    print (s.twoSum([2,7,11,15], 9))
