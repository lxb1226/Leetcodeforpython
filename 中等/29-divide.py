class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp,cnt = divisor,1
            while dividend >= tmp:
                tmp <<= 1
                cnt <<= 1
            dividend -= tmp >> 1
            res += cnt >> 1
        res = res if positive else -res
        # if res >= 2**31 -1:
        #     return 2**32 -1
        # elif res <= -(2**31):
        #     return -(2**31)
        # else:
        #     return res
        return min(max(-(2**31),res),2**31-1)
    
if __name__ == "__main__":
    solution = Solution()
    dividend = 10
    divisor = 3
    res = solution.divide(dividend,divisor)
    print(res)