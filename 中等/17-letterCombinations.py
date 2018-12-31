class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # d = {
        #     '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        # }
       
        # tmp = ['']
        # res = []
        # for i in range(len(digits)):
        #     res = []
        #     s1 = digits[i]
        #     value = d[s1] 
        #     for s in value:
        #         for x in tmp:
        #             res.append(s+x)  
        #     tmp = res

        # return res

        lookup = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res = []
        
        def helper(s, digits):
            if len(digits) == 0:
                res.append(s)
            else:
                cur_digit = digits[0]
                for char in lookup[cur_digit]:
                    helper(s+char, digits[1:])
                    
        if not digits or len(digits) == 0:
            return res
        helper('', digits)
        return res

        

if __name__ == "__main__":
    solution = Solution()
    s = '23'
    res = solution.letterCombinations(s)           
    print(res)
                    
