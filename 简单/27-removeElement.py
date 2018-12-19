class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 解法一：
        # 参考26题的思路
        # 比较列表中的每个元素,如果等于val,那么进入下一个循环,否则将这个元素的值赋给nums[idx]
        # idx表示的是不是val的值得个数 -1


        # idx = 0
        # for num in nums:
        #     if num != val:
        #         nums[idx] = num
        #         idx += 1
        # return idx

        # 解法二
        # 简单粗暴
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    # nums = [3,2,2,3]
    # val = 3
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = solution.removeElement(nums,val)
    print(nums)
    print(result)