class Solution:
    def mySqrt(self, x: int) -> int:
        left = 2
        right = x//2
        if x<2:
            return x
        while left<=right:
            
            mid = (left + right)//2
            
            if mid**2 == x:
                return mid
            elif mid**2<x:
                left = mid+1
            else:
                right = mid-1
            
        return right
            
# Why are we returning right?
# Draw out the example for finding the sqaure root for 10 and you'll know why
