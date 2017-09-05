# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        root = new_node = ListNode(0)
        
        while l1 or l2 or carry:
            
            value1 = value2 = 0
            if l1:
                value1 = l1.val
                l1 = l1.next
                
            if l2:
                value2 = l2.val
                l2 = l2.next
                
            carry, val = divmod(value1+value2+carry, 10)
            new_node.next = ListNode(val)
            new_node = new_node.next
            
        return root.next