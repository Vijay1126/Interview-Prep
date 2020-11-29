class Solution:
     def mostCompetitive(self, A, k):
        stack = []
        
        for index, value in enumerate(A):
            
            while stack and stack[-1]>value and len(stack)-1+len(A)-index>=k:
                stack.pop()
            if len(stack)<k:
                stack.append(value)
        
        return stack
