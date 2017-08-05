class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) <= 1:
            return False
        
        compliments = {} 
        
        for i in range(len(nums)):
            if nums[i] in compliments: 
                return [compliments[nums[i]], i]
            else: 
                compliment = target-nums[i]
                compliments[compliment] = i 
           