class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: -x[1])
        ans = 0
        for i in boxTypes:
            if truckSize>i[0]:
                truckSize-=i[0]
                ans+=i[1]*i[0]
            else:
                ans+=truckSize*i[1]
                return ans
        
        return ans
