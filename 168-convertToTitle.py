class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        ans = ''
        while n:
            ans = chr(ord('A') + (n-1)%26) + ans
            n = (n-1)//26
        return ans


        
if __name__ == "__main__":
    solution = Solution()
    n = 702
    result = solution.convertToTitle(n)
    print(result)