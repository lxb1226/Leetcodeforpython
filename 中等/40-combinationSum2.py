class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(remainer,comb,idx):
            if remainer < 0:
                return 
            if remainer == 0 and comb not in res:
                res.append(comb)
                return
            if idx >= len(candidates):
                return
            helper(remainer,comb,idx+1)
            helper(remainer-candidates[idx],comb+[candidates[idx]],idx+1)

        res = []
        candidates.sort()
        helper(target,[],0)
        return res

if __name__ == "__main__":
    solution = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = solution.combinationSum2(candidates,target)
    print(res)