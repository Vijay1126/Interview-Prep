class Solution:
    def reorganizeString(self, S: str) -> str:
        
        count = Counter(S)
        
        heap = [[-count[i], i] for i in count]
        heapify(heap)

        maxCount = -heap[0][0]
        if (len(S)+1)//2<maxCount:
            return ""
        index = 0
        output = ["" for _ in range(len(S))]
        while heap:
            count, letter = heappop(heap)
            count*=-1
            for i in range(count):
                if index>=len(S):
                    index = 1
                output[index] = letter
                index+=2
                
        return "".join(output)
    
