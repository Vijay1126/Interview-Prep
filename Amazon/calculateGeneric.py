class Solution:
    def calculate(self, s: str) -> int:
        
        self.index = 0 
  
        def helper(s):
            sign = "+"
            num = 0
            stack = []
            while self.index<len(s):
                curr = s[self.index]
                if curr.isdigit():
                    num = num * 10 + ord(curr) - ord("0")
                if curr == "(":
                    self.index+=1
                    num = helper(s)
                if curr in ["+", "-", "/", "*", ")"] or self.index == len(s) - 1:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "/":
                        stack[-1] = stack[-1]//num if stack[-1]>0 else -(-stack[-1]//num)
                    elif sign == "*":
                        stack[-1] = stack[-1]*num
                    if curr == ")":
                        return sum(stack)
                    sign = curr
                    num = 0
                self.index+=1
                
            return sum(stack)
        
        return helper(s)
                
                    
                    
                    
