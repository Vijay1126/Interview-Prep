class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        prime = 7
        
        hashValues = {}
        currVal = 0
        LENGTH = 10
        for i in range(LENGTH):
            currVal += ord(s)*prime**i
        hashValue[currVal] = 1
        
        output = []
        def updateHashValue(dropValue, addvalue, currValue):
            return (currValue - dropValue)/prime + addValue*prime**(LENGTH-1)
            
        
        for i in range(1,len(s) - LENGTH):
            currVal = updateHashValue(ord(s[i-1]),  ord(s[i+LENGTH-1]), currVal)
            if currVal in hashValues:
                output.append(s[i:i+LENGTH])            
            hashValues[currVal] = 1
        
        return output
            
            
