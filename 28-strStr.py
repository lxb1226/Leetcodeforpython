class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 解法一：O(m*n),空间复杂度O(1)
        # 暴力解法


        # if not needle or len(needle) == 0:
        #     return 0
        # for i in range(len(haystack)-len(needle)+1):
        #     if needle[0] == haystack[i]:
        #         j = 1
        #         while j<len(needle) and haystack[i+j] == needle[j]:
        #             j += 1
        #         if j == len(needle):
        #             return i
        # return -1

        # 解法二：
        # 调用python的内置函数
        # return haystack.find(needle)

        # 解法三：KMP算法  留待之后来看
        # 时间复杂度O(m+n),空间复杂度O(n)
        text, pattern = haystack, needle
        if not pattern or len(pattern) == 0:
            return 0
        
        lps = self.findLPS(pattern) # longest proper prefix which is also suffix
        i, j = 0, 0 # idx for text and pattern
        res = -1
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                res = i - j
                return res
                j = lps[j-1]
            elif i < len(text) and pattern[j] != text[i]: # mismatch after j matches 
                if j != 0: # Don't match lps[0..lps[j-1]] characters, they will match anyway 
                    j = lps[j-1]
                else:
                    i += 1  
        return res

    def findLPS(self, pattern): 
        length, lps = 0, [0]
        for i in range(1, len(pattern)):
            while length > 0 and pattern[length] != pattern[i]:
                length = lps[length-1]
            if pattern[length] == pattern[i]:
                length += 1
            lps.append(length)
        return lps




if __name__ == "__main__":
    solution = Solution()
    haystack = 'hello'
    needle = 'll'
    # haystack = "aaaaa"
    # needle = "bba"
    result = solution.strStr(haystack,needle)
    print(result)
            

            


            
            
             
        