class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 解法一：动态规划
        ## 实质是求出前n-1个数的最大自序和。
        # n = len(nums)
        # maxSum = [nums[0] for i in range(n)]
        # for i in range(1,n):
        #     maxSum[i] = max(maxSum[i-1]+nums[i],nums[i])
        # print(maxSum)
        # return max(maxSum)    

        ## 解法二：分治算法
        #   
        def find_max_crossing_subarray(nums,low,mid,high):
            left_sum = float('-inf')
            sum = 0
            for i in range(mid,low-1,-1):
                sum += nums[i]
                if sum > left_sum:
                    left_sum = sum
            right_num = float('-inf')
            sum = 0
            for j in range(mid+1,high+1):
                sum += nums[j]
                if sum > right_num:
                    right_sum = sum
            return left_sum + right_sum
        
        def find_max_subarray(nums,low,high):
            if low == high:
                return nums[low]
            else:
                mid = (low+high)//2
                left_sum = find_max_subarray(nums,low,mid)
                right_sum = find_max_subarray(nums,mid+1,high)
                cross_sum = find_max_crossing_subarray(nums,low,mid,high)
                print('left_sum:{},right_sum:{},cross_num:{}'.format(left_sum,right_sum,cross_sum))
                print('mid:{},low:{},high:{}'.format(mid,low,high))
                return max(left_sum,right_sum,cross_sum)
        return find_max_subarray(nums,0,len(nums)-1)





if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solution.maxSubArray(nums)
    print(result)