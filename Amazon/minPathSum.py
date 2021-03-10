class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        matrix = [[ 0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for j in range(len(matrix[0])):
            matrix[0][j] = grid[0][j]+matrix[0][j-1] if j!=0 else grid[0][j]
            
        for i in range(len(matrix)):
            matrix[i][0] = grid[i][0]+matrix[i-1][0] if i!=0 else grid[i][0]
            
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                matrix[row][col] = grid[row][col] + min(matrix[row-1][col], matrix[row][col-1])
        
        print(matrix)
        return matrix[-1][-1]                
