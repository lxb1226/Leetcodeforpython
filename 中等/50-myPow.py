class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if n<0:
        #     x = 1/x
        #     n = -n
        # res = 1
        # while n:
        #     if n&1:
        #         res *= x
        #     x *= x
        #     n >>= 1
        # return res

        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n&1:
            return x*self.myPow(x*x,n>>1)
        else:
            return self.myPow(x*x,n>>1)


   
          
        
       
        


if __name__ == "__main__":
    solution = Solution()
    x = 3
    n = -1
    res = solution.myPow(x,n)
    print(res)