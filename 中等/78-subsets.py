class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = [[]]
        # for num in nums:
        #     res.extend([tmp+[num] for tmp in res])
        # return res


        # res = []
        # def search(tmp_res,idx):
        #     if idx == len(nums):
        #         res.append(tmp_res)
        #     else:
        #         search(tmp_res+[nums[idx]],idx+1)
        #         search(tmp_res,idx+1)
        
        # search([],0)
        # return res

        res = []
        def dfs(depth,start,lst):
            res.append(lst)
            if depth == len(nums):
                return
            for i in range(start,len(nums)):
                dfs(depth+1,i+1,lst+[nums[i]])
        dfs(0,0,[])
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    res = solution.subsets(nums)
    print(res)
                



                