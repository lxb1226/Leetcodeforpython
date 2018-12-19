class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #解法一
        #比较前一个和后一个的做法,如果相同则删除,不然就加1
        # 时间复杂度O(N^2)
        # idx = 0
        # while idx < len(nums) -1:
        #     if nums[idx] == nums[idx+1]:
        #         nums.pop(idx)
        #     else:
        #         idx += 1
        # return len(nums)

        # 解法二
        # 找到不重复的元素
        # 时间复杂度O(N)

        idx = 0
        for num in nums:
            if idx < 1 or num != nums[idx-1]:
                nums[idx] = num
                idx += 1
        return idx
            



if __name__ == "__main__":
    solution = Solution()
    # nums = [1,1,2,2,2,3,3,4]
    nums = [0,0,1,1,1,2,2,3,3,4]
    # nums = [1,1,2]
    result = solution.removeDuplicates(nums)
    print(result)
    print(nums)

            
            
