class Trie:
    def __init__(self):
        self.map = {}
        
    def add(self, word):
        start = self.map
        for letter in word:
            if letter not in start:
                start[letter] = {}
            start = start[letter]
        start["$"] = {}
    
    def search(self,word):
        start = self.map
        for letter in word:
            if letter not in start:
                return False
            start = start[letter]
        return "$" in start 
    
    def getRoot(self):
        return self.map
    
    def getWords(self, currWord):
        
        def helper(curr, word):
            nonlocal output   
            if '$' in curr:
                output.append(word)
            for letter in curr:
                helper(curr[letter], word+letter)
            
            return (output[:3])
        start = self.map
        for letter in currWord:
            output = []
            if letter not in start:
                return []
            else:
                start = start[letter]
            
        return helper(start, currWord)
    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        myTrie = Trie()
        products.sort()
        for product in products:
            myTrie.add(product)
        
        root = myTrie.getRoot()
        ans = []
        curr = ""
        for letter in searchWord:
            curr+=letter
            ans.append(myTrie.getWords(curr))
        return ans
                    
        
