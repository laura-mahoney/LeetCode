class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        
        n = str(bin(n))
        
        for i in n:
            if i == '1':
                count += 1
                
        return count