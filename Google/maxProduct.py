class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maximum , minimum = nums[0], nums[0]
        result = maximum
        for num in nums[1:]:
            
            temp = max(num, num*maximum, num*minimum)
            minimum = min(num, num*maximum, num*minimum)
            
            maximum = temp 
            result = max(maximum, result)
        
        return result
