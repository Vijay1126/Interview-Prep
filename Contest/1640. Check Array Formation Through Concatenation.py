class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        # setArr = set(arr)
        indexDict = defaultdict(int)
        for index, value in enumerate(pieces):
            for num in value:
                indexDict[num] = index
                break
    
        mainIndex = 0
        while mainIndex<len(arr):
            
            if arr[mainIndex] in indexDict:
                i = 0
                pArr = pieces[indexDict[arr[mainIndex]]]
                while i<len(pArr) and mainIndex<len(arr):
                    if arr[mainIndex]!=pArr[i]:
                        return False
                    i+=1
                    mainIndex+=1
            else:
                return False
                    
        return True
                    
