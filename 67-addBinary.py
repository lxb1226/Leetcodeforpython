class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
    
            
        
        # if a == '' or b == '':
        #     return a+b
        # if a[-1] == '0' and b[-1] == '0':
        #     return self.addBinary(a[:-1],b[:-1]) + '0'
        # elif a[-1] == '1' and b[-1] == '1':
        #     return self.addBinary(a[:-1],self.addBinary(b[:-1],'1')) + '0'
        # else:
        #     return self.addBinary(a[:-1],b[:-1]) + '1'


        # 解法二：
        # return bin(int(a,2)+int(b,2))[2:]

    
if __name__ == "__main__":
    solution = Solution()
    # a = '11'
    # b = '1'
    # a = '1010'
    # b = '1011'
    a = '100'
    b = '110010'
    result = solution.addBinary(a,b)
    print(result)


                
                
                
                
                
                
                
