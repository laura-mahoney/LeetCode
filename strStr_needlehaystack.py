class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for hay in range(len(haystack)): 
            if haystack[hay] == needle:
                return hay
    
        return -1