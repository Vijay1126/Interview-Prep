class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        operand = "+"
        i= 0
        while i<len(s):
            curr = s[i]
            if curr == " ":
                i+=1
                continue
            if curr.isdigit():
                num = 0
                while i<len(s) and s[i].isdigit():
                    # print(s[i])
                    num = num *10 + int(s[i])
                    i+=1
                curr = num
                # print(num)
                if operand in "+-":
                    if operand == "+":
                        stack.append(int(curr))
                    else:
                        stack.append(-int(curr))
                elif operand == "*":
                    oldDigit = stack.pop()
                    stack.append(oldDigit*int(curr))
                elif operand == "/":
                    oldDigit = stack.pop()
                    sign = "-" if oldDigit<0 else "+"
                    toAdd = -oldDigit//int(curr) if oldDigit<0 else oldDigit//int(curr)
                    if sign == "-":
                        stack.append(-toAdd)
                    else:
                        stack.append(toAdd)
                        
                    
            else:
                operand = curr
                i+=1
        print(stack)
        return sum(stack)
