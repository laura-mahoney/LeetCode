# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        current = head
        previous = None
        
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next 
            
        return previous