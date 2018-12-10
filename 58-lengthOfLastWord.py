class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法一
        # strs = s.split(' ')
        # for i in range(len(strs)-1,-1,-1):
        #     if strs[i] is not '':
        #         return len(strs[i])
        # return 0

        # 解法二：
        # 将字符串中的所有字符倒过来，再去掉前后的空格
        # s = s[::-1].strip()
        # print(s)
        # return s.find(' ') if s.find(' ') != -1 else len(s)

        # 解法三：
        # split()方法值得注意,最少可以分0组,且是一空格为分隔符
        # split(" ")最少可以分1组
        lst = s.split()
        if len(lst) >=1:
            return len(lst[-1])
        return 0

        # 解法四：
        # 相当于是解法一的进阶版
        return len(s.strip().split(" ")[-1])

        
        

if __name__ == "__main__":
    solution = Solution()
    strs = ['hello world','a  ','a ']
    for s in strs:
        result = solution.lengthOfLastWord(s)
        print(result)