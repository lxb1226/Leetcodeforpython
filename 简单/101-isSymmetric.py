# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 解法一：
        # 思路:对左边的树左序遍历，对右边的树右序遍历，如果最后结果一样，就是对称的
        
        
        # if not root or not (left or right):
        #     return True
        # left = root.left
        # right = root.right
        # return  self.isSameTree(left,right)

        # 解法二：
        # 迭代

        lst = []
        lst.append(root)
        lst.append(root)
        while lst:
            t1 = lst.pop() if lst else None
            t2 = lst.pop() if lst else None
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            lst.append(t1.left)
            lst.append(t2.right)
            lst.append(t1.right)
            lst.append(t2.left)
        return True


    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        return p.val == q.val and self.isSameTree(p.left,q.right) and self.isSameTree(p.right,q.left)  

