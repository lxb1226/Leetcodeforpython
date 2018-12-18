class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        ## 暴力法
        ## 超出时间限制

        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]

        ## 二分法加上双指针
        l,r = 0,len(numbers) - 1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
            



    
if __name__ == "__main__":
    solution = Solution()
    # numbers = [2,7,11,5]
    
    # target = 9
    numbers = [2,3,4]
    target = 6
    result = solution.twoSum(numbers,target)
    print(result)