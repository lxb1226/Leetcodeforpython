class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        curNum = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        maxUp = maxLeft = 0
        maxDown = n - 1
        maxRight = n - 1
        direction = 0
        while True:
            if direction == 0:# go right
                for i in range(maxLeft,maxRight+1):
                    curNum += 1
                    matrix[maxUp][i] = curNum
                maxUp += 1
            elif direction == 1:# go down
                for i in range(maxUp,maxDown+1):
                    curNum += 1
                    matrix[i][maxRight] = curNum
                maxRight -= 1
            elif direction == 2:# go left
                for i in reversed(range(maxLeft,maxRight+1)):
                    curNum += 1
                    matrix[maxDown][i] = curNum
                maxDown -=1
            else: # go up
                for i in reversed(range(maxUp,maxDown+1)):
                    curNum += 1
                    matrix[i][maxLeft] = curNum
                maxLeft += 1
            if curNum >= n*n:
                return matrix
            direction = (direction+1)%4

if __name__ == "__main__":
    solution = Solution()
    n = 3
    res = solution.generateMatrix(n)
    print(res)
