class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(digits)-1, -1, -1):
            carry = 0
            if digits[i] + 1 + carry <= 9:
                digits[i] = digits[i] + 1 + carry
                return digits
            else:
                total = digits[i] + carry + 1
                carry, digits[i] = divmod(total, 10)

        digits.insert(0,1)
        return digits