from functools import lru_cache
class Solution:
    def minDifficulty(self, arr: List[int], d: int) -> int:        
        if len(arr)<d:
            return -1
        @lru_cache(None)
        def helper(index, daysLeft):
            if daysLeft == 1:
                return max(arr[index:])
            currMax = arr[index]
            minimumTime = float("inf")
            for i in range(index, len(arr)-daysLeft+1):
                currMax = max(currMax, arr[i])
                minimumTime = min(minimumTime, currMax + helper(i+1, daysLeft-1))    
            return minimumTime
        return helper(0, d)
                
