class Solution:
    def toLowerCase(self, str: str) -> str:
        output = ""
        for index, value in enumerate(str):
            if 65<=ord(value)<=90:
                output+=chr(ord(value)+32)
            else:
                output+=value
        return output
                
