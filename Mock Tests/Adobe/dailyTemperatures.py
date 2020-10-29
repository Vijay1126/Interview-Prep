class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        stack = []
        output = [0]*len(T)
        
        for i in range(len(T)):
            if not stack:
                stack.append((T[i],i))
            else:
                while stack and stack[-1][0]<T[i]:
                    output[stack[-1][1]] = i-stack[-1][1]
                    stack.pop()
                stack.append((T[i],i))
        return output
                
