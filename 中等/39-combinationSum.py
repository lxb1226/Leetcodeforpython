class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(remain,combi,idx):
            if remain < 0:
                return
            if remain == 0:
                res.append(combi)
                return 
            if idx>= len(candidates):
                return
            helper(remain,combi,idx+1)
            helper(remain-candidates[idx],combi+[candidates[idx]],idx)
        res = []
        helper(target,[],0)
        return res
    
if __name__ == "__main__":
    solution = Solution()
    candidates = [2,3,6,7]
    target = 7
    res = solution.combinationSum(candidates,target)
    print(res)