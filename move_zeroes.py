class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        number = len(nums)
        
        i = 0 
        
        while i < number:
            
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                number -= 1
                
            else:
                
                i += 1