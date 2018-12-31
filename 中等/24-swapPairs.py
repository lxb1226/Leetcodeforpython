# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head or head.next:
            return head
        p = head.next
        while head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            head = head.next
        return p

        
        