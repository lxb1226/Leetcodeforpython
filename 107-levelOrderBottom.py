# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 解法一：
        # 递归

        def dfs(node,level,res):
            if not node:
                return 
            if len(res) < level:
                res.append([])
            res[level-1].append(node.val)
            dfs(node.left,level+1,res)
            dfs(node.right,level+1,res)
        res = []
        dfs(root,1,res)
        return res[::-1]

        # 解法二：
        # 迭代
        if not root:
            return []
        cur_level = [root]
        res = []
        while cur_level:
            nxt_level = []
            tmp_res = []
            for node in cur_level:
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
                tmp_res.append(node.val)
            cur_level = nxt_level
            res.append(tmp_res)
        return res[::-1]


        
            

            
            

    


    





        
        