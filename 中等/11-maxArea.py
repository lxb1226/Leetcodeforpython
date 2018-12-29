class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,len(height) - 1
        maxarea = 0
        while i!=j:
            tmp  = min(height[i],height[j]) * (j-i)
            if tmp > maxarea:
                maxarea = tmp
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return maxarea
    

if __name__ == "__main__":
    solution = Solution()

    height = [1,8,6,2,5,4,8,3,7]
    result = solution.maxArea(height)
    print(result)

