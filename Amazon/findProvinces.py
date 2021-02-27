class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        
        connections = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    connections[i].append(j)
                    connections[j].append(j)
                
        
        visited = set()
        number = 0
    
        def dfs(startingCity):
            visited.add(startingCity)
            for city in connections[startingCity]:
                if city not in visited:
                    dfs(city)
            return 1
                
        for i in range(len(grid)):
            if i not in visited:
                number+= dfs(i)
        
        return number
    
            
            
