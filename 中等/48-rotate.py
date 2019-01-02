class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # c = len(matrix)
        # matrix[:] = [[matrix[c-i-1][j] for i in range(c)] for j in range(c)]
        
        # n = len(matrix)
        # # 上下翻转
        # for i in range(n//2):
        #     matrix[i],matrix[n-1-i] = matrix[n-1-i],matrix[i]
        # # 主对角线翻转
        # for i in range(i+1,n):
        #     for j in range(i+1,n):
        #         matrix[i][j],matrix[j][i] =  matrix[j][i],matrix[i][j]
        

        matrix[:] = zip(*matrix[::-1])

if __name__ == "__main__":
    solution = Solution()
    matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    solution.rotate(matrix)
    print(matrix)



