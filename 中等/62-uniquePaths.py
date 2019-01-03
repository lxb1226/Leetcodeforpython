class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # if m == 1:
        #     return 1
        # if n == 1:
        #     return 1
        # return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

        # if m < 1 or n < 1:
        #     return 0
        # dp=[[1]*n for i in range(m)]
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[-1][-1]
        

        # if m < 1 or n < 1:
        #     return 0
        # dp = [1]*n
        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[j] += dp[j-1]
        # return dp[n-1]

        import math
        return math.factorial(m+n-2)//math.factorial(n-1)//math.factorial(m-1)


if __name__ == "__main__":
    solution = Solution()
    m = 7
    n = 3
    res = solution.uniquePaths(m,n)
    print(res)

