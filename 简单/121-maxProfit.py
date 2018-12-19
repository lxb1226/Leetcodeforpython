class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        ## 暴力解法
        ## 超时
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         diff = prices[j] - prices[i]
        #         if diff >profit:
        #             profit = diff
        # return profit

        ## 解法一

        # if not prices or len(prices) == 0:
        #     return 0
        # opt = [0]*len(prices)
        # for i in range(1,len(prices)):
        #     opt[i] = max(opt[i-1]+prices[i]-prices[i-1],0)
        #     print(opt[i])
        # return max(opt)

        


if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)
    print(result)



    