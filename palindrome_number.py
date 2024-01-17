class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        
        m=str(x)
        txt = m[::-1]
        return txt==m
        """
        :type x: int
        :rtype: bool
        """
