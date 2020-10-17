class Solution:
    def numTimesAllBlue(self, A):
        ans = 0
        right = 0
        on = 0
        for i in A:
            on+=1
            right = max(right, i)
            ans += right==on
        return ans
            
