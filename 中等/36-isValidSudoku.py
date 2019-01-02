class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            lookup_row = {}
            lookup_col = {}
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in lookup_row or not 1 <= int(board[i][j]) <= 9:
                        return False
                lookup_row[board[i][j]] = 1
                if board[j][i] != '.':
                    if board[j][i] in lookup_col or not 1 <= int(board[j][i]) <=9:
                        return False
                lookup_col[board[j][i]] = 1

        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.check(i,j,board):
                    return False
        return True

    def check(self,x,y,board):
        lookup = {}
        for i in range(x,x+3):
            for j in range(y,y+3):
                if board[i][j] != '.':
                    if board[i][j] in lookup or not 1<= int(board[i][j]) <= 9:
                        return False
            lookup[board[i][j]] = 1
        return True
    
if __name__ == "__main__":
    solution = Solution()
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    res = solution.isValidSudoku(board)
    print(res)
