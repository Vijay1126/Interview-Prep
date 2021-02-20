class Solution:
    def maxArea(self, h: int, w: int, hi: List[int], v: List[int]) -> int:
        
        hi.extend([0,h])
        v.extend([0,w])
        hi.sort()
        v.sort()
        
        maxH = max([hi[i+1]-hi[i] for i in range(len(hi)-1)])
        maxV = max([v[i+1]-v[i] for i in range(len(v)-1)])
        return (maxV*maxH)%(10**9 + 7)
