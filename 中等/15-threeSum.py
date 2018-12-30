class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # n,res = len(nums),[]
        # nums.sort()
        # for i in range(n):
        #     if i>0 and nums[i] == nums[i-1]:
        #         continue
        #     l,r = i+1,n-1
        #     while l<r:
        #         tmp = nums[i] + nums[l] + nums[r]
        #         if tmp == 0:
        #             res.append([nums[i],nums[l],nums[r]])
        #             l += 1
        #             r -= 1
        #             while l<r and nums[l] == nums[l-1]:
        #                 l += 1
        #             while l<r and nums[r] == nums[r+1]:
        #                 r -= 1
        #         elif tmp >0:
        #             r -= 1
        #         else:
        #             l += 1
        # return res


        nums_hash = {}
        result = list()
        for num in nums:
            nums_hash[num] = nums_hash.get(num,0) + 1
        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0,0,0])
        nums = sorted(list(nums_hash.keys()))

        for i,num in enumerate(nums):
            for j in nums[i+1:]:
                if num*2 + j == 0 and nums_hash[num] >= 2:
                    result.append([num,num,j])
                if j*2 + num == 0 and nums_hash[j] >= 2:
                    result.append([j,j,num])
                dif = 0 - num - j
                if dif > j and dif in nums_hash:
                    result.append([num,j,dif])
        return result

        


if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    res = solution.threeSum(nums)
    print(res)