class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            curr = heights[i+1]-heights[i]
            if curr>0:
                heapq.heappush(heap, curr)
            if len(heap)>ladders:
                bricks-=heapq.heappop(heap)
            if bricks<0:
                return i
        return len(heights)-1
