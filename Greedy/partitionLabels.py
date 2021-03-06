class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        hashMap = {value: index for index,value in enumerate(S)}
        
        # print(hashmap)
        left = 0
        right = 1
        currEnd = hashMap[S[left]]
        output = []
        anchor = 0
        for index, value in enumerate(S):
            currEnd = max(currEnd, hashMap[value])
            if index == currEnd:
                output.append(index-anchor+1)
                anchor = index+1
        
        return output
                
