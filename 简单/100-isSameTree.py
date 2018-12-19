# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ## 解法一：
        ## 递归

        # if not p and not q:
        #     return True
        # if (p and not q) or (not p and q):
        #     return False
        # return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)   

        # 一行代码版本
        return p.val == q.val and all(map(self.isSameTree,(p.left,p.right),(q.left,q.right))) if p and q else p is q
        





        
        