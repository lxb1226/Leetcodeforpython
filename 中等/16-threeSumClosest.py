import time
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # n,res,diff = len(nums),None,float('inf')
        # nums.sort()
        # for i in range(n):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue
        #     l,r = i+1,n-1
        #     while l<r:
        #         tmp = nums[i] + nums[l] + nums[r]
        #         if tmp == target:
        #             return target
        #         elif tmp > target:
        #             r -= 1
        #             if abs(tmp - target) < diff:
        #                 diff = abs(tmp-target)
        #                 res = tmp
        #             while l < r and nums[r] == nums[r+1]:
        #                 r -= 1
        #         else:
        #             l += 1
        #             if abs(tmp - target) < diff:
        #                 diff = abs(tmp - target)
        #                 res = tmp
        #             while l < r and nums[l] == nums[l-1]:
        #                 l += 1
        # return res

        nums.sort()
        res = sum(nums[:3])
        # m = abs(res - target)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l<r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == target:
                    return target
                if abs(res-target) > abs(temp-target):
                    res = temp
                elif target < temp:
                    r -= 1
                else:
                    l += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [-1,2,1,-4]
    target = 1
    start = time.time()
    res = solution.threeSumClosest(nums,target)
    end = time.time()
    print("用了: ",end-start)
    print(res)




