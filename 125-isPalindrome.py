class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 一开始的答案
        # length = len(s)
        # i,j = 0,length-1
        # while i < length//2:
        #         while j >= length//2:
        #             if s[i].isdigit() or s[i].isalpha():
        #                 if s[j].isdigit() or s[j].isalpha():
        #                     if s[i].upper() == s[j].upper():
        #                         i += 1
        #                         j -= 1
        #                     else:
        #                         return False
        #                 else:
        #                     j -= 1
        #             else:
        #                 i += 1
        # return True

        # 解法一：
        # 比较reversed string 和原本的是否相等
        # new = ''
        # s = s.lower()
        # for i in s:
        #     if '0' <= i <= '9' or 'a' <= i <= 'z':
        #         new += i
        # return new == new[::-1]

        # 另一种写法
        # s = ''.join(e for e in s if e.isalnum()).lower()
        # return s == s[::-1]

        # 解法二：
        # 利用正则 re.sub()
        # import re
        # s = re.sub('[^0-9a-z-A-z]+','',s).lower()
        # return s == s[::-1]

        # 解法三:
        #  双指针 in-place

        l,r = 0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True




if __name__ == "__main__":
    solution = Solution()
    # s = 'A man, a plan, a canal: Panama'
    s = 'a.'
    result = solution.isPalindrome(s)
    print(result)

            
            
        