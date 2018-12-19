class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        ## 解法一

        # k = k % len(nums)
        # if k!=0:
        #     tmp = nums[-k:]
        #     for j in range(len(nums)-1,k-1,-1):
        #         nums[j] = nums[j-k]
        #     nums[:k] = tmp

        ## 解法二
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


        

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution.rotate(nums, k)
    print(nums)