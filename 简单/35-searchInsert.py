class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 解法一：
        # i从0到nums的长做循环,
        # 1.如果 nums[i]<target，那么就作下一个循环
        # 2.不然就return i
        # 3.如果target超过了nums中的最大值,那么就把它插入到最后一位，也就是return len(nums)
        # for i in range(len(nums)):
        #     if nums[i]<target:
        #         i += 1
        #     else:
        #         return i
        # return len(nums)

        # 解法二：
        # 二分法
        # 时间复杂度O(lgN),
        l,r = 0,len(nums)-1
        while l<=r:
            # mid = l+((r-1)>>1)
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        return l

            


if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,5,6]
    target = 5
    # target = 2
    # target = 7
    # target = 0
    result = solution.searchInsert(nums,target)
    print(result)
            
        