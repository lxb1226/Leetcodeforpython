class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        l,r = 0,m*n-1
        while l<=r:
            mid = (l+r)//2
            i = mid//n 
            j = mid % n 
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

        # if not matrix or not matrix[0]:
        #     return False
        
        # row = len(matrix)
        # col = len(matrix[0]) if row else 0
        # l,r = 0,row - 1
        # while l<=r:
        #     mid_row = (l+r)//2
        #     if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
        #         m,n = 0,col - 1
        #         while m <= n:
        #             mid_col = (m+n)//2
        #             if matrix[mid_row][mid_col] > target:
        #                 n = mid_col - 1
        #             elif matrix[mid_row][mid_col] < target:
        #                 m = mid_col + 1
        #             else:
        #                 return True
        #         return False
        #     elif target < matrix[mid_row][0]:
        #         r = mid_row - 1
        #     else:
        #         l = mid_row + 1

        # return False



if __name__ == "__main__":
    solution = Solution()
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    # target = 13
    matrix = [[1]]
    target = 1
    res = solution.searchMatrix(matrix,target)
    print(res)

