class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        leftHigh = [-float("inf") for _ in range(len(height))]
        currMax = height[0]
        for index, value in enumerate(height[1:]):
            leftHigh[index+1] = currMax
            currMax = max(currMax, value)
        currMax = height[-1]
        output = 0
        for index, value in enumerate(reversed(height[:-1])):
            output += max(min(leftHigh[len(height)-index-1], currMax)-value,0)
            currMax = max(currMax, value)
        return output
            
