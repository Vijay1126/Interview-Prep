class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0]*60
        output = 0
        for i in time:
            output+= count[-i%60]
            
            count[i%60]+=1
        return output
