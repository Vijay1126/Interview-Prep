# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        
		length = len(string)
		for i in range(length-1, -1, -1):
			
			word = string[i:]
			print(word)
			start = self.root
			for letter in word:
				if letter not in start:
					start[letter] = {}
				start = start[letter]
			start["*"] = True


    def contains(self, string):
        start = self.root
		for letter in string:
			if letter not in start:
				return False
			start = start[letter]
		
		return "*" in start 
