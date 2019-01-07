class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        # res = [[]]

        # for i in range(len(nums)):
        #     res.extend([tmp+[nums[i]] for tmp in res if tmp.count(nums[i]) == i - nums.index(nums[i])])
        # return res

        # res = [[]]
        # for i in range(len(nums)):
        #     res.extend([tmp + [nums[i]] for tmp in res if tmp.count(nums[i]) == nums[:i].count(nums[i])])
        # return res

        # nums.sort()
        # res = [[]]
        # tmp_size = 0
        # for i in range(len(nums)):
        #     start = tmp_size if i >= 1 and nums[i] == nums[i-1] else 0
        #     tmp_size = len(res)
        #     for j in range(start,tmp_size):
        #         res.append([nums[i]]+res[j])
        # return res


        # nums.sort()
        # res = []
        # def dfs(depth,start,lst):
        #     if lst not in res:
        #         res.append(lst)
        #     if depth == len(nums):
        #         return
        #     for i in range(start,len(nums)):
        #         dfs(depth+1,i+1,lst+[nums[i]])
        
        # dfs(0,0,[])
        # return res


        # nums.sort()
        # res = []

        # def search(cur_lst,idx):
        #     if idx == len(nums):
        #         if cur_lst not in res:
        #             res.append(cur_lst)
        #         return
        #     search(cur_lst + [nums[idx]],idx+1)
        #     search(cur_lst,idx+1)
        
        # search([],0)
        # return res
        

if __name__ == "__main__": 
    solution = Solution()
    nums = [1,2,2]
    res = solution.subsetsWithDup(nums)
    print(res)