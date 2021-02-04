class Trie:
	def __init__(self):
		self.root = {}
		self.endingWord = "*"
	
	def addWords(self, word):
		start = self.root
		for letter in word:
			if letter not in start:
				start[letter] = {}
			start = start[letter]
		start[self.endingWord] = word

def checkIfStringIn(string, i, trie, present):
	start = trie.root
	for letter in string[i:]:
		if letter == "k":
			print(i)
		if letter in start:
			start = start[letter]
		else:
			break
		if "*" in start:
			present.add(start["*"])
		
	
def multiStringSearch(bigString, smallStrings):
	myTrie = Trie()
	for word in smallStrings:
		myTrie.addWords(word)
	presentMap = set()
	for i in range(len(bigString)):
		checkIfStringIn(bigString, i, myTrie, presentMap)
	print(presentMap)
	return [string in presentMap for string in smallStrings]
		
	
