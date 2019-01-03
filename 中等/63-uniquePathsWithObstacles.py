class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        
        # if obstacleGrid[0][0] == 1:
        #     return 0
        # obstacleGrid[0][0] = 1
        # for i in range(1,m):
        #     obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # for j in range(1,n):
        #     obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        
        # for i in range(1,m):
        #     for j in range(1,n):
        #         if obstacleGrid[i][j] == 0:
        #             obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        #         else:
        #             obstacleGrid[i][j] = 0
        
        # return obstacleGrid[m-1][n-1]

        # self.res = 0
        # def travel(x,y):
        #     if x == len(obstacleGrid)  - 1 and y == len(obstacleGrid[0]) - 1 and obstacleGrid[x][y] != 1:
        #         self.res += 1
        #     if x + 1 <= len(obstacleGrid) - 1 and obstacleGrid[x+1][y] != 1:
        #         travel(x+1,y)
        #     if y + 1 <= len(obstacleGrid[0]) - 1 and obstacleGrid[x][y+1] != 1:
        #         travel(x,y+1)
        
        # if obstacleGrid[0][0] == 1:
        #     return 0
        # travel(0,0)
        # return self.res

        cache = {}
        def travel(x,y):
            if (x,y) in cache:
                return cache[x,y]
            res = 0
            if obstacleGrid[x][y] == 0:
                if x+1<=len(obstacleGrid) - 1:
                    res += travel(x+1,y)
                if y+1<=len(obstacleGrid[0]) - 1:
                    res += travel(x,y+1)
                if x==len(obstacleGrid)- 1 and y == len(obstacleGrid[0]) - 1:
                    res += 1
            cache[x,y] = res
            return cache[x,y]
        if obstacleGrid[0][0] == 1:
            return 0
        return travel(0,0)
        
        


if __name__ == "__main__":
    solution = Solution()
    obstacleGrid = [[0,0],[1,1],[0,0]]
    res = solution.uniquePathsWithObstacles(obstacleGrid)
    print(res)