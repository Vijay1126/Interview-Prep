class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for value in ops:
            
            if value.lstrip('-').isdigit():
                stack.append(int(value))
            elif value == "+":
                stack.append(stack[-1]+ stack[-2])
            elif value == "D":
                
                stack.append(stack[-1]*2)
            elif value == "C":
                stack.pop()
        return sum(stack)
