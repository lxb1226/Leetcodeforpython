# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    # 1.如果l1或者l2为空,那么返回另外一个
    # 2.比较l1和l2中元素的大小,小的放入创建的链表中
    # 3.最后一定会有一个链表的元素空了，那么将另外一个链表的所有元素赋值给创建的链表

        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next


if __name__ == "__main__":
    
    solution = Solution()
    L = solution.mergeTwoLists(l1,l2)
    while L != None:
        print(L.val)
        L = L.next
