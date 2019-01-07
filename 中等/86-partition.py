# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1_start = dummy1_end = ListNode(None)
        dummy2_start = dummy2_end = ListNode(None)
        while head:
            if head.val < x:
                dummy1_end.next = head
                dummy1_end = dummy1_end.next
            else:
                dummy2_end.next = head
                dummy2_end = dummy2_end.next
            
            head = head.next
        dummy2_end.next = None
        dummy1_end.next = dummy2_start.next

        return dummy1_start.next
    