class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        rows = len(board)
        cols = len(board[0])
        directions = [[0,1], [1,0],[-1,0],[0,-1]]
        #Iterating through the matrix
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    board[i][j] = None
                    if self.wordPresent(i, j, word[1:], rows, cols, directions, board ):
                        return True
                    board[i][j] = word[0]
                    
        return False

    def wordPresent(self, i, j, word, rows, cols, directions, board):
        #Base Case:
        if not word:
            return True
        else:
            currLetter = word[0]
            for a, b in directions:
                nextRow, nextCol = i+a, j+b
                if 0<=nextRow<rows and 0<=nextCol<cols and board[nextRow][nextCol] == currLetter:
                    #Action
                    board[nextRow][nextCol] = None
                    
                    #Recurse
                    if self.wordPresent(nextRow, nextCol, word[1:], rows, cols, directions,  board):                
                        return True
                    
                    #Back the fuck track
                    board[nextRow][nextCol] = currLetter
                
            return False
        
Time: Length * 3^L
SPace : L
        
        
        
