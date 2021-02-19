class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        queue = deque([])
        output = []
        for index, value in enumerate(nums):
            while queue and nums[queue[-1]]<value:
                queue.pop()
            
            if queue and index-queue[0]>=k:
                queue.popleft()
            queue.append(index)
            output.append(nums[queue[0]])
            
        return output[k-1:]
