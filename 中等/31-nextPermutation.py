class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        idx = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                idx = i
                break
        if idx != 0:
            for i in range(len(nums)-1,idx-1,-1):
                if nums[i] > nums[idx-1]:
                    nums[i],nums[idx-1] = nums[idx-1],nums[i]
                    break
        nums[idx:] = nums[idx:][::-1]
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,4,6,5,3]
    solution.nextPermutation(nums)
    print(nums)