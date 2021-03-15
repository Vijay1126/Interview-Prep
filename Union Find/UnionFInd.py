class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1 for i in range(n)] 
    
    def find(self, i):
        parent = self.parent[i] 
        if parent!=i:
            parent = self.find(self.parent[i])
        self.parent[i] = parent
        return parent
    
    def union(self, a, b):
        firstParent, secondParent = map(self.find, (a,b))
        if firstParent != secondParent:
            small, big = sorted([firstParent, secondParent], key = lambda x: self.rank[x])
            self.parent[small] = big
            self.rank[big] += self.rank[small]
            
    @property
    def getRank(self):
        return self.rank
    
    @property
    def getParent(self):
        return self.parent
    
    def getNumberOfComponents(self):
        parents = [self.find(i) for i in range(self.n)]
        return len(Counter(parents))
            
        
            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
            myUnionFind = UnionFind(n)
            for a,b in edges:
                myUnionFind.union(a,b)
            return myUnionFind.getNumberOfComponents()
            
            
