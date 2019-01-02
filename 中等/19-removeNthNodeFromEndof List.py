# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy,lst = head,[0]*(n+1)
        # # idx = 0
        # while head:
        #     lst = lst[1:]
        #     lst.append(head)
        #     head = head.next
        # if lst[0]:
        #     if n == 1:
        #         lst[0].next = None
        #         return dummy
        #     lst[0].next = lst[2]
        #     return dummy
        # else:
        #     return dummy.next


        # slow = fast = dummy = ListNode(-1)
        # dummy.next = head
        # for _ in range(n):
        #     fast = fast.next
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        
        # slow.next = slow.next.next
        # return dummy.next

        slow = fast = dummy = ListNode(-1)
        dummy.next = head
        count = 0
        while fast.next:
            if count <n:
                count += 1
                fast = fast.next
            else:
                fast = fast.next
                slow = slow.next

        slow.next = slow.next.next
        return dummy.next