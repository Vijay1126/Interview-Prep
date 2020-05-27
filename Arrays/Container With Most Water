class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        maxArea = -float('inf')
        right = len(height)-1
        while (left<right):
            length = min(height[left],height[right])
            maxArea = max(maxArea,(right-left)*length)
            if height[right]>height[left]:
                left+=1
            elif height[right]==height[left] :
                right-=1
                left+=1
            else:
                right-=1
            
        return maxArea
