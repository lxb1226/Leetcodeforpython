class Solution:
    cache = {
        1:1,
        2:2
    }
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 解法一：递归
        # 思路同解法二

        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cache[n]


        # 解法二：
        # 思路:因为只能爬1步或者2步，那么n个台阶就等于一开始爬1步的方法加上一开始爬2步的方法
        # 这样就只需要计算n-1个台阶和n-2个台阶的方法

        cache = [1]*(n+1)
        for i in range(2,n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[-1]
        
    
if __name__ == "__main__":
    solution = Solution()
    n = 10
    result = solution.climbStairs(n)
    print(solution.cache)
    print(result)
    
        