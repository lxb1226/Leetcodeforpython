class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # 暴力解法 但会超出时间限制
        # i = 0
        # while i * i <= x:
        #     if i*i <= x and (i+1)*(1+i) > x:
        #         return i
        #     i += 1


        # 二分法
        # if x == 1:
        #     return 1
        # if x == 0:
        #     return 0
        # l,r = 0,x
        # while l<r:
        #     mid = (l+r)//2
        #     # print(mid)
        #     if mid*mid <= x and (mid+1)*(mid+1) > x:
        #         return mid
        #     elif mid*mid > x:
        #         r = mid
        #     else:
        #         l = mid + 1

        # 牛顿法
        # 时间复杂度lg(N)
        t = x
        while t*t >x:
            t = (t+x/t)//2
        return int(t)


if __name__ == "__main__":
    solution = Solution()
    for x in range(0,10):
        result = solution.mySqrt(x)
        print(result)
        
