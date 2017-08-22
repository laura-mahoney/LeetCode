class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        majority = len(nums)/2
        
        num_dict = {}
        
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            
        for key, value in num_dict.items():
            if value > majority:
                return key
