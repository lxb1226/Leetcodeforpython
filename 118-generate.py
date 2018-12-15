class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # yhtriangle = []
        # yhtriangle.append([1])
        # if numRows == 1:
        #     return yhtriangle
        # yhtriangle.append([1,1])
        # if numRows == 2:
        #     return yhtriangle
        # for i in range(3,numRows+1):
        #     L = [1,1]
        #     temp = yhtriangle[-1]
        #     for j in range(1,i-1):
        #         a = temp[j-1] + temp[j]
        #         L.insert(j,a)
        #     yhtriangle.append(L)
        # return yhtriangle


        # 同上面解法 但代码更简洁

        # if numRows == 0:
        #     return []
        # res = [[1]]
        # for i in range(1,numRows):
        #     tmp = [1]
        #     for j in range(1,i):
        #         tmp.append(res[-1][j-1]+res[-1][j])
        #     tmp.append(1)
        #     res.append(tmp)
        # return res


        # 无话可说的代码
        # 简洁到了...
        res = [[1]]
        for i in range(1,numRows):
            res.append(list(map(lambda x,y:x+y,[0]+res[-1],res[-1]+[0])))
        return res[:numRows]


            
if __name__ == "__main__":
    solution = Solution()
    L = solution.generate(5)
    print(L)

    
    