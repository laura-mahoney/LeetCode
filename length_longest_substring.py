class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
                
        if len(s) == 1:
            return 1

        if len(s) == 0:
            return 0
        
        start = 0
        maximum_length = 0
        used_chars = {}
        
        #loop over the string
        for i in range(len(s)):
            #if this character is in used_chars and
            #if this characters last index is greater than the start,
            #update start to be the last index that char was used in
            if s[i] in used_chars and start<=used_chars[s[i]]:
                #if the character is in used_chars, it is a reapeat char, 
                #start must be updated as the last position that char was found at
                #plus one, i.e. the next char
                start = used_chars[s[i]] + 1
                
            else:
                maximum_length = max(maximum_length, i-start+1)
                
            used_chars[s[i]] = i #saves all chars and their most recent index
          
          return maximum_length
                