# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 解法一：
        # 思路同二叉树的最大深度，需要注意的是如果根节点的左右节点有一个为空，那么最小的深度应该是以另外一个节点为根节点的树的深度+1
        

        if not root:
            return 0 
        if not root.left:
            return  self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left),self.minDepth(root.right)) + 1

