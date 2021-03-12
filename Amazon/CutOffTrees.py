class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        sourceRow, sourceColumn = 0, 0
        
        treeLocations = sorted([[rowIndex,columnIndex] for rowIndex, row in enumerate(forest) 
                                                for columnIndex, value in enumerate(row) 
                                                if value>1 ], key = lambda x : forest[x[0]][x[1]])
        totalDistance = 0
        for destinationRow, destinationColumn in treeLocations:
            distance = self.getDistance(forest, sourceRow, sourceColumn, destinationRow, destinationColumn)
            if distance == -1:
                return -1
            else:
                totalDistance += distance
            sourceRow, sourceColumn = destinationRow, destinationColumn
        return totalDistance
 
    def getDistance(self, forest, sourceRow, sourceColumn, destinationRow, destinationColumn):
        cost = defaultdict(lambda: float("inf"))
        cost[(sourceRow, sourceColumn)] = 0
        heap = [(0, 0, sourceRow, sourceColumn)]
        
        while heap:
            heuristicValue, gValue,  row, column = heapq.heappop(heap)
            if row == destinationRow and column == destinationColumn:
                return gValue
            for nextRow, nextCol in [[row+1,column], [row, column+1], [row-1, column], [row, column-1]]:
                if 0<=nextRow<len(forest) and 0<=nextCol<len(forest[0]) and forest[nextRow][nextCol]>1:
                    newCost = gValue + 1 + abs(destinationRow-nextRow) + abs(destinationColumn-nextCol)
                    if newCost < cost[(nextRow, nextCol)]:
                        cost[(nextRow, nextCol)] = newCost 
                        heapq.heappush(heap, (newCost, gValue+1,nextRow, nextCol))
            
            
        return -1
