class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 解法一：
        # leftBrackets = '([{'
        # rightBrackets = ')]}'
        # stack = []

        # for i in s:
        #     if i in leftBrackets:
        #         stack.append(i)
        #     if i in rightBrackets:
        #         if not stack:
        #             return False
        #         tmp = stack.pop()
        #         if i == ')' and tmp != '(':
        #             return False
        #         if i == ']' and tmp != '[':
        #             return False
        #         if i == '}' and tmp != '{':
        #             return False
        # return stack == []      


        # 解法二： 遍历字符串s,如果属于leftBrackets,那么就加入堆栈stack,如果属于rightBrackets,首先看堆栈是否是空
        # 如果堆栈为空,则说明前面没有左括号,返回False，
        # 否则删除并弹出堆栈中的最后一个,如果能够匹配,那么进行下一轮循环,否则返回False
        # 解法一同解法二：

        # leftBrackets = ['(','[','{']
        leftBrackets = '([{'
        rightBrackets = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i in leftBrackets:
                stack.append(i)
            if i in rightBrackets:
                if not stack:
                    return False
                tmp = stack.pop()
                if rightBrackets[i] != tmp:
                    return False
        return stack == []



            
if __name__ == "__main__":
    solution = Solution()
    # strs = '({})'
    strs = [']','()','()[]{}','(]','([)]','{[]}']
    for str in strs:
        result = solution.isValid(str)
        print(result)
    