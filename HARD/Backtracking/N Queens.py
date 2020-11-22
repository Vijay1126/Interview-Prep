class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        board = [[0 for i in range(n)] for i in range(n)]
        def isSafe(i,j, board):
            row = i
            while row>=0:
                if board[row][j]==1:
                    print("Enter")
                    return False
                row-=1
            row, col = i, j
            while row>=0 and col>=0:
                
                if board[row][col] == 1:
                    return False
                row -=1
                col-=1
            row , col = i, j
            while row>=0 and col<n:
                
                if board[row][col] == 1:
                    return False
                row -=1
                col+=1
            return True
        def helper(board, number, i):
            if number == n:
                temp = []
                for a in range(n):
                    currStr = ""
                    for b in range(n):
                        if board[a][b]==1:
                            currStr+="Q"
                        else:
                            currStr+="."
                    temp.append(currStr)
                output.append(temp)
            else:
                for j in range(n):
                    if isSafe(i,j, board):
                        number+=1
                        board[i][j]=1
                        helper(board, i+1, number)
                        board[i][j]=0
                        number-=1
            return output    
        return helper(board, 0, 0)

