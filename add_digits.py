class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        
        return self.addDigits(sum(map(int, str(num)))) if num >=10 else num
        
        #using magic 9, i.e. digital root