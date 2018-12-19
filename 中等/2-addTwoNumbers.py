# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class LList:
#     def __init__(self):
#         self.head = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ## 将链表转化成数字，再做加法
        ## 再把和转换成链表
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        
        # val1,val2 = [l1.val],[l2.val]
        # while l1.next:
        #     val1.append(l1.next.val)
        #     l1 = l1.next
        # while l2.next:
        #     val2.append(l2.next.val)
        #     l2 = l2.next
        
        # num1 = ''.join([str(i) for i in val1[::-1]])
        # num2 = ''.join([str(i) for i in val2[::-1]])
        # tmp = str(int(num1) + int(num2))
        # res = ListNode(int(temp[0]))
        # run_res = res
        # for i in range(1,len(tmp)):
        #     run_res.next = ListNode(int(tmp[i]))
        #     run_res = run_res.next
        # return res

    
        ## 递归的思想
        ## 最棒的在于处理1的地方
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1

        # if l1.val + l2.val <10:
        #     l3 = ListNode(l1.val+l2.val)
        #     l3.next = self.addTwoNumbers(l1.next,l2.next)
        # else:
        #     13 = ListNode(l1.val+l2.val-10)
        #     tmp = ListNode(1)
        #     tmp.next = None
        #     l3.next = self.addTwoNumbers(l1.next,self.addTwoNumbers(l2.next,tmp))
        # return l3

            

                

                

        