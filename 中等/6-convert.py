class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >=len(s):
            return s

        res = [''] * numRows
        idx,step = 0,1
        
        for x in s:
            res[idx] += x
            # print(idx,step,res)
            if idx == 0:
                step = 1
            elif idx == numRows-1:
                step = -1
            idx += step
        
        return ''.join(res)

        

if __name__ == "__main__":
    solution = Solution()
    s = 'LEETCODEISHIRING'
    numRows = 4
    result = solution.convert(s,numRows)
    print(result)
