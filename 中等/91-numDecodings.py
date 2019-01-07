class Solution:
    # cnt = 0
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
    #     if s == "" or s[0] == '0':
    #         return 0
    #     self.combine(s)
    #     return self.cnt

    # def combine(self,s):
    #     if len(s) == 1 or len(s) == 0:
    #         self.cnt += 1
    #         return
    #     else:
    #         if int(s[0]) <= 26:
    #             self.combine(s[1:])
    #         if  int(s[:2]) <= 26:
    #             self.combine(s[2:])

        if not s or len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == '0':
            return 0
        elif len(s) == 1 and s[0] != '0':
            return 1

        dp = [0] * len(s)
        dp[0] = 1 if s[0] != '0' else 0

        if 10 <= int(s[:2]) <= 26:
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = dp[0]
        for i in range(2,len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

        



if __name__ == "__main__":
    s = '27'
    solution = Solution()
    res = solution.numDecodings(s)
    print(res)
        
