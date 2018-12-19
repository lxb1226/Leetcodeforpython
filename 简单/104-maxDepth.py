# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 解法一：
        # 利用递归,如果root为0，那么return 0
        # 不然就返回root的左节点和右节点中的最大值 + 1
        # 终于可以自己想出递归出来了，不容易不容易
        
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
        

        # 一行代码版本
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1 if root else 0