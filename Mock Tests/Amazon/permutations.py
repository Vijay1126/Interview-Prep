class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(first, curr):
            nonlocal output 
            if first == len(nums):
                output.append(curr[:])
            else:
                for i in range(first,len(nums)):
                    curr[i], curr[first] = curr[first], curr[i]
                    helper(first+1, curr)
                    curr[i], curr[first] = curr[first], curr[i]
                return output
        return helper(0, nums)
                    
