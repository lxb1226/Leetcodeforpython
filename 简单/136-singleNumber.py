class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解法一：
        # 对于nums中的不同数字建立一个字典，统计它们的个数

        # d = {}
        # for x in nums:
        #     score = 1
        #     if x in d.keys():
        #         d[x] += score
        #     else:
        #         d[x] = score
        # return list(d.keys())[list(d.values()).index(1)] 

        # 解法二：
        # 位运算
        # 将所有数字进行异或操作即可
        # 一个整数与自己异或的结果是0
        # 一个整数与0异或的结果是自己
        # 异或操作满足交换律

        res = nums[0]       
        for i in nums[1:]:
            res ^= i
        return res



if __name__ == "__main__":
    solution = Solution()
    nums = [4,1,2,1,2]
    result = solution.singleNumber(nums)
    print(result)