class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # b = list('{:032b}'.format(n))
        # for i in range(16):
        #     b[i],b[31-i] = b[31-i],b[i]
        # r = int(''.join(b),2)
        # return r
        ## 将32位无符号二进制变成字符串形式
        ## 再将字符串翻转就好了
        b = list('{:032b}'.format(n))
        return int(b[::-1],2)        


if __name__ == "__main__":
    solution = Solution()
    n = 00000010100101000001111010011100
    result = solution.reverseBits(n)
    print(result)


