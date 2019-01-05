class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        l,r = 0,len(nums) - 1
        while l<=r:
            while l<r and nums[l] == nums[r]:
                l += 1
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False

if __name__ == "__main__":
    solution = Solution()
    # nums = [2,5,6,0,0,1,2]
    # nums = [0,0,1,1,2,0]
    nums = [3,1,1]
    target = 3
    res = solution.search(nums,target)
    print(res)




