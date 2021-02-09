class Solution:
    def numberToWords(self, num: int) -> str:
        
        upto20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        upto100 = ["", "Ten","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        hundreds = ["", "Thousand", "Million", "Billion"]
        
        def helper(num):
            if num == 0:
                return ""
            elif num<20:
                return upto20[num] + " "
            elif num<100:
                print(num//10, num )
                return upto100[num//10] + " " + helper(num%10)
            else:
                return helper(num//100)+ "Hundred " + helper(num%100)
        
        
        if num == 0:
            return "Zero"
        output = ""
        for index, value in enumerate(hundreds):
            
            curr = num%1000
            if curr!=0:
                output =  helper(curr) + value + " "+ output
            
            num//=1000
        return output.strip()
                
Edge Cases: Input as Zero // Spaces to be added, how the arrays are stored, 
        
