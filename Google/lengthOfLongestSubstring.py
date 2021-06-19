class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0, 0
        currentLetters = set()
        output = 0
        while j<len(s):
            if s[j] in currentLetters:
                currentLetters.remove(s[i])
                i+=1
            else:
                currentLetters.add(s[j])
                j+=1
                output = max(output, len(currentLetters))
        return output
                
                
        
        
