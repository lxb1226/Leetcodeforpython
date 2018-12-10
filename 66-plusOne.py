class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 解法一：
        # 思路是把数组转换成数字去运算，最后转换回来

        # length = len(digits)
        # sum = 0
        # # for i,num in enumerate(digits):
        # #     sum += num * 10**(length-i-1)
        # # 这种做法使用的时间更少，更少的乘法
        # for i in range(length):
        #     sum = sum*10 + digits[i]
        # return  list(map(int,str(sum+1)))

        # 解法二：
        # 运用递归,如果为空,那么直接return[1]
        # 如果最后一位小于9，那么直接加1
        # 如果最后一位等于9，那么递归前几位
        # 但用到了，所以时间花销比较大
        # if digits == []:
        #     return [1]
        # if digits[-1] < 9:
        #     return digits[:-1] + [digits[-1]+1]
        # else:
        #     return self.plusOne(digits[:-1])+[0]

        # 解法三
        # 用循环解决，时间花销和解法一差不多
        # 十分巧妙的方法
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
                break
            else:
                digits[i] -= 10
        if carry == 1:
            digits.insert(0,1)
        return digits
    

    

if __name__ == "__main__":
    solution = Solution()
    digits = [1,2,3]
    # digits = [9,9,9]
    result = solution.plusOne(digits)
    print(result)
        
