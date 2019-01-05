class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        # def dfs(cur_cums,idx):
        #     if len(cur_cums)  == k:
        #         self.res.append(cur_cums)
        #         return 
        #     if idx == n + 1:
        #         return 
        #     dfs(cur_cums+[idx],idx+1)
        #     dfs(cur_cums,idx+1)
        # self.res = []
        # dfs([],1)
        # return self.res

        if k == n or k == 0:
            return [[i for i in range(1,k+1)]]
        res = self.combine(n-1,k-1)
        res = [lst+[n] for lst in res]
        res.extend(self.combine(n-1,k))
        return res

    

if __name__ == "__main__":
    solution = Solution()
    n = 4
    k = 2
    res = solution.combine(n,k)
    print(res)
