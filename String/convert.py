class Solution:
    def convert(self, s: str, numRows: int) -> str:
        up = False
        
        output = [""]*(numRows)
        counter = 0
        if numRows == 1:
            return s
        for i in range(len(s)):
            if up:
                output[numRows-counter-1]+=s[i]
            else:
                output[counter]+=s[i]
            counter+=1
            if counter == numRows-1:
                up = not up
                counter = 0
        
        return "".join(output)
