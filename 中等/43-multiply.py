class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # def str2int(num):
        #     res = 0
        #     for i in range(len(num)-1,-1,-1):
        #         res += int(num[i]) * pow(10,len(num)-1-i)
        #     return res
        # return str(str2int(num1)*str2int(num2))

        lookup = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9} # 节省查找时间，避免无休止使用ord函数来得到数字
        if num1 == '0' or num2 == '0':
            return '0'
        num1, num2 = num1[::-1], num2[::-1]
        
        tmp_res = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp_res[i+j] += lookup[num1[i]] * lookup[num2[j]]

        res = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)+len(num2)):
            res[i] = tmp_res[i] % 10
            if i < len(num1)+len(num2)-1:
                tmp_res[i+1] += tmp_res[i]//10 
        return ''.join(str(i) for i in res[::-1]).lstrip('0')  # 去掉最终结果头部可能存在的‘0’             
                
                

if __name__ == "__main__":
    solution = Solution()
    num1 = '91'
    num2 = '91'
    res = solution.multiply(num1,num2)
    print(res)