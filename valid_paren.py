class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        paren = {')': '(', '}': '{', ']': '['}
        stack = []
        
        if len(s) < 2: 
            return False 
        
        for char in s:
            
            if char in paren.values():
                stack.append(char)
            elif char in paren.keys():
                if stack == [] or stack.pop() != paren[char]:
                    return False
            else:
                return False
            
        return stack == []
                    