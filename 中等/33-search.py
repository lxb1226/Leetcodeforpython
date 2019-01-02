class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
        return -1

if __name__ == "__main__":
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 2
    res = solution.search(nums,target)
    print(res)