from heapq import *
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if not A:
            return A
        rows = len(A)
        cols = len(A[0])
        destination = [rows-1, cols-1]
        heap = [(-A[0][0], self.distance([0,0],destination),0,0)]
        visited = set()
        
        while heap:
            currDistance, _, i, j = heapq.heappop(heap)
            
            if [i,j] == destination:
                return -currDistance
            if (i,j) not in visited:
                visited.add((i,j))
                directions = [[i+1,j], [i,j+1], [i,j-1],[i-1,j]]
                for nextRow, nextCol in directions:
                    if 0<=nextRow<rows and 0<=nextCol<cols and (nextRow,nextCol) not in visited:
                        nextVal = max(-A[nextRow][nextCol], currDistance)
                        heapq.heappush(heap, (nextVal, self.distance([nextRow,nextCol],destination),nextRow,nextCol))

    def distance(self, a , b ):
        return abs(a[0]-b[0]) + abs(a[1]+b[1])
