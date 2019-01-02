class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return [-1,-1]
        res = []
        l,r = 0,len(nums) -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target and (mid == 0 or nums[mid-1]!=target):
                res.append(mid)
                break
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid -1
        if not res:
            return [-1,-1]

        r = len(nums) - 1
        while l<=r:
            mid = (l+r) //2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1]!=target):
                res.append(mid)
                break
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    # nums = [5,5,7,8,8,10]
    nums = [2,2]
    target = 2
    res = solution.searchRange(nums,target)
    print(res)