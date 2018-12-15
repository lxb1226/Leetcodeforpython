class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # res = [[1]]
        # for i in range(1,rowIndex+1):
        #     res.append(list(map(lambda x,y:x+y,[0]+res[-1],res[-1]+[0])))
        # return res[rowIndex]

        res = [1]
        for i in range(1,rowIndex+1):
            tmp = [1]
            for j in range(1,i):
                tmp.append(res[j-1]+res[j])
            tmp.append(1)
            res = tmp
        return res

if __name__ == "__main__":
    solution = Solution()
    result = solution.getRow(3)
    print(result)