class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        解法一：
        1.当strs为空时,返回空字符串
        2.一次假设从0到len(strs[0]),在每一轮循环中：
            1.如果strs中存在string比当前长度i还小,那么返回strs[0][:i]
            2.如果strs存在index字符与LCP字符不同，则返回上一个LCP,返回strs[0][:i]
        """
        # if not strs:
        #     return ''
        # for i in range(len(strs[0])):
        #     for str in strs:
        #         if len(str)<=i or strs[0][i] != str[i]:
        #             return strs[0][:i]
        # return str[0]

        """
        解法二：创建一个len(strs)大小的列表，里面全是strs[0]
        然后i从1到len(strs),如果strs[i]不以strs[0]为前缀,那么strs[0]删掉最后一位


        """
        # if not strs:
        #     return ''
        # dp = [strs[0]] * len(strs)
        # for i in range(1,len(strs)):
        #     while not strs[i].startswith(dp[i-1]):
        #         dp[i-1] = dp[i-1][:-1]
        #     dp[i] = dp[i-1]
        # return dp[-1]

        """
        解法三：
        os.path.commonprefix()
        """
        import os
        return os.path.commonprefix(strs)


if __name__ == "__main__":

    strs = ['flower','flow','flight']
    strs1 = ["dog","racecar","car"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    # result = solution.longestCommonPrefix(strs1)

    print(result)
