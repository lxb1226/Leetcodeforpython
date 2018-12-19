class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base,res = 5,0
        # while n>= base:
        #     res += n//base
        #     base *= 5
        # return res

        ## 判断n的因子中有多少个5即可
        count = 0
        while n>0:
            count += n//5
            n = n//5
        return count 


if __name__ == "__main__":
    solution = Solution()
    n = 25
    result = solution.trailingZeroes(n)
    print(result)