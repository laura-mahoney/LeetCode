class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        numbers = set()
        
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in numbers:
                return False
            else:
                numbers.add(n)
        return True
        