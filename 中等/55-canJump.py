class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # def helper(idx):
        #     if idx==0:
        #         return True
        #     for i in range(idx):
        #         if nums[i]>=idx-1:
        #             if helper(i):
        #                 return True
        #     return False
        # return helper(len(nums)-1)

        # if not nums or len(nums)<=1:
        #     return True
        # for i in range(len(nums)-2,-1,-1):
        #     if nums[i]==0:
        #         possible = False
        #         for j in range(0,i):
        #             if nums[j]+j >i:
        #                 possible = True
        #                 break
        #         if not possible:
        #             return False
        # return True

        if not nums or len(nums) <=1:
            return True
        max_jump = 0
        for i in range(len(nums)):
            max_jump = max(max_jump-1,nums[i])
            if max_jump + i >= len(nums) -1:
                return True
            if max_jump <= 0:
                return False

    
    

if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,1,1,4]
    # nums = [0]
    # nums = [3,2,1,0,4]
    # nums = [1,2]
    res = solution.canJump(nums)
    print(res)



