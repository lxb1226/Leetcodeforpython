class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # red,white = 0,0
        # for i in nums:
        #     if i == 0:
        #         red += 1
        #     elif i == 1:
        #         white += 1
        # for i in range(red):
        #     nums[i] = 0
        # for i in range(red,red+white):
        #     nums[i] = 1
        # for i in range(red+white,len(nums)):
        #     nums[i] = 2

        # begin,cur,end = 0,0,len(nums) - 1
        # while cur <= end:
        #     if nums[cur] == 0:
        #         nums[begin],nums[cur] = nums[cur],nums[begin]
        #         cur += 1
        #         begin += 1
        #     elif nums[cur] == 1:
        #         cur += 1
        #     else:
        #         nums[cur],nums[end] = nums[end],nums[cur]
        #         end -= 1


        # i,l,r = 0,0,len(nums) - 1
        # while i < len(nums):
        #     if nums[i] == 2 and i < r:
        #         nums[i],nums[r] = nums[r],2
        #         r -= 1
        #     elif nums[i] == 0 and i >= l:
        #         nums[i],nums[l] = nums[l],0
        #         l += 1
        #     else:
        #         i += 1

        n0,n1,n2 = -1,-1,-1
        for i in range(len(nums)):
            if nums[i] == 0:
                n0,n1,n2 = n0+1, n1+1, n2+1
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
            elif nums[i] == 1:
                n1,n2 = n1+1,n2+1
                nums[n2] = 2
                nums[n1] = 1
            else:
                n2 += 1
                nums[n2] = 2            
        
        

        
if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    solution = Solution()
    solution.sortColors(nums)
    print(nums)