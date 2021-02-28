class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left>=0 and right<len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return (s[left+1: right], right-left-1)
            
        output = [0, 0]
        currMax = [0, 0]
        for i in range(len(s)):
            first = expand(i, i)
            second = expand(i, i+1)
            if first[1]>second[1]:
                currMax = first
            else:
                currMax = second
            if currMax[1]>output[1]:
                output = currMax
           
        return output[0]
