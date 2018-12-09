class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 解法一：
        # 1.如果n=1，那么返回'1'
        # 2.如果n>1,先递归算前n-1个,
        

        # if n==1:
        #     return '1'
        # s = self.countAndSay(n-1) + '*'
        # res,count = '',1
        # for i in range(len(s)-1):
        #     if s[i] == s[i+1]:
        #         count += 1
        #     else:
        #         res += str(count) + str(s[i])
        #         count = 1
        # return res

        # 解法二：
        # import itertools
        res = '1'
        for i in range(n-1):
            res = ''.join([str(len(list(group))) + digit for digit,group in itertools.groupby(res)])
        return res
            
if __name__ == "__main__":
    solution = Solution()
    n = 4
    result = solution.countAndSay(n)
    print(result)
                

                


            
