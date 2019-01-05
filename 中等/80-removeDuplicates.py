class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        # if not nums:
        #     return 0
        # if len(nums) <= 2:
        #     return len(nums)
        # idx = 0
        # while idx < len(nums) - 1:
        #     if nums[idx] == nums[idx+1] == nums[idx+2]:
        #         nums.pop(idx)
        #     else:
        #         idx += 1
        # return len(nums)

        idx = 0
        for num in nums:
            if idx < 2 or num > nums[idx-2]:
                nums[idx] = num
                idx += 1
        return idx

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,2,2,3]
    res = solution.removeDuplicates(nums)
    print(res)
    print(nums)