class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(0,len(s)):
            num += (ord(s[len(s)-1-i])-64)*(26**i)
        return num
    
if __name__ == "__main__":
    solution = Solution()
    s = 'ZY'
    result = solution.titleToNumber(s)
    print(result)
        

