class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # def lcs(s1,s2):
        #     m = [[0]*(1+len(s2)) for i in range(1+len(s1))]
        #     longest,x_longest = 0,0
        #     for x in range(1,1+len(s1)):
        #         for y in range(1,1+len(s2)):
        #             if s1[x-1] == s2[y-1]:
        #                 m[x][y] = m[x-1][y-1] + 1
        #                 if m[x][y] > longest:
        #                     longest = m[x][y]
        #                     x_longest = x
        #                 else:
        #                     m[x][y] = 0
        #     return s1[x_longest-longest:x_longest]

        # return lcs(s,s[::-1])

        # n = len(s)
        # # 空或者一个字符时，直接返回
        # if n < 2:
        #     return s
        
        # l = 0
        # r = 0
        # m = 0
        # c = 0
        # b = True
        # for i in range(n):
        #     for j in range(min(n - i, i + 1)):
        #         if s[i - j] != s[i + j]:
        #             b = False
        #             break
        #         else:
        #             c = 2 * j + 1

        #     if c > m:
        #         l = i - j + 1 - b
        #         r = i + j + b
        #         m = c
        #     b = True

        #     for j in range(min(n - i - 1, i + 1)):
        #         if (s[i - j] != s[i + j + 1]):
        #             b = False
        #             break
        #         else:
        #             c = 2 * j + 2

        #     if (c > m):
        #         l = i - j + 1 - b
        #         r = i + j + 1 + b
        #         m = c
        #     b = True
        # return s[l:r]


    



if __name__ == "__main__":
    solution = Solution()
    s = 'babad'
    result = solution.longestPalindrome(s)
    print(result)
