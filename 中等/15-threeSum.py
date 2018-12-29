class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         result = -1*(nums[i] + nums[j])
        #         if result in nums and  result != nums[i] and result!= nums[j]:
        #             res.append([nums[i],nums[j],result])
        # return res
        n,res = len(nums),[]
        nums.sort()
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,n-1
            while l<r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif tmp >0:
                    r -= 1
                else:
                    l += 1
        return res



if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    res = solution.threeSum(nums)
    print(res)