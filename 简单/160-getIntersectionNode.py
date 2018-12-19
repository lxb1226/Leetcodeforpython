# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 定义两个指针，第一轮让两个到达末尾的节点指向另一个链表的头部，最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
## 两个指针等于移动了相同的距离，有交点就返回，无交点就是各走了两条指针的长度

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
        
