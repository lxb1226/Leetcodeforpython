# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ## 解法一:
        ## 思路：和删除有序数组的重复元素一样,判断前面一个和后面一个的值是否相同,如果相同,删除,不然就往下走

        # dummy = head
        # if head == None or head.next == None:
        #     return head
        # while head.next != None:
        #     if head.val == head.next.val:
        #         head.next = head.next.next
        #     else:
        #         head = head.next
        # return dummy

        ## 解法一的另一种写法
        ## 更简洁
        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return dummy

        ## 解法二
        if not head:
            return head
        dummy = prev = ListNode(None)
        while head:
            if head.val == prev.val:
                if not head.next:
                    prev.next = None
            else:
                prev.next = head
                prev = prev.next
        return dummy.next
        

    