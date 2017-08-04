class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        

        if len(s) == 0 or len(s) == 1 or len(s) == 2:
            return len(s)

        start = longest = 0
        sub_dict = {}

        for i in range(len(s)):

            if s[i] in sub_dict

            sub_dict[s[i]] = i
