class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]
            rest = nums[:i] + nums[i+1:]
            for j in self.permute(rest):
                if [prefix]+j not in res:
                    res.append([prefix]+j)
        return res

if __name__ == "__main__":
    solution = Solution()
    # nums = [1,2,3]
    nums = [1,1,2]
    res = solution.permute(nums)
    print(res)