class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        heap = [(0,0,0)]
        
        visited = set()
        rows = len(heights)
        cols = len(heights[0])
        output = -float("inf")
        while heap:
            
            costSoFar, row, col = heapq.heappop(heap)
            output = max(costSoFar, output)
            if row == rows-1 and col == cols-1:
                return output
            
            visited.add((row, col))
            for nextRow, nextCol in [[row+1, col],[row-1, col], [row, col+1], [row, col-1]]:
                if 0<=nextRow<rows and 0<=nextCol<cols and (nextRow, nextCol) not in visited:
                    heapq.heappush(heap, (abs(heights[row][col]-heights[nextRow][nextCol]), nextRow, nextCol))
        
        return 0
            
            
