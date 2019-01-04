class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        
        # m = len(matrix)
        # n = len(matrix[0])

        # tmp = [[matrix[i][j] for j in range(n)] for i in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if tmp[i][j] == 0:
        #             for y in range(n):
        #                 matrix[i][y] = 0
        #             for x in range(m):
        #                 matrix[x][j] = 0

        # m = len(matrix)
        # n = len(matrix[0])

        # l,c = [0]*m,[0]*n

        # for i in range(m):
        #     if 0 in matrix[i]:
        #         l[i] = 1
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[j][i] == 0:
        #             c[i] = 1
        #             continue
        
        # for i in range(m):
        #     for j in range(n):
        #         if l[i] == 1 or c[j] == 1:
        #             matrix[i][j] = 0
        
        # import sys
        # sign = sys.maxsize
        # row = len(matrix)
        # col = len(matrix[0]) if row else 0

        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == 0:
        #             for k in range(col):
        #                 matrix[i][k] = sign if matrix[i][k] != 0 else 0
        #             for k in range(row):
        #                 matrix[k][j] = sign if matrix[k][j] != 0 else 0
        
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == sign:
        #             matrix[i][j] = 0


        row = len(matrix)
        col = len(matrix[0]) if row else 0

        set_first_col = False
        for i in range(row):
            if matrix[i][0] == 0:
                set_first_col = True
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][0] == 0 or matrix[j][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0

        if set_first_col:
            for i in range(row):
                matrix[i][0] = 0

        


if __name__ == "__main__":
    solution = Solution()
    matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
    solution.setZeroes(matrix)
    print(matrix)
