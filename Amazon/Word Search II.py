
class Trie:
    def __init__(self):
        self.root = {}
        
    def addWord(self, word):
        start = self.root
        for letter in word:
            if letter not in start:
                start[letter] = {}
            start = start[letter]
        start["*"] = word #This word is present and it ends here
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i,j, root):
                letter = board[i][j]
                nextLevel = (root[letter])
                
                    
                found = nextLevel.pop("*", False)
                if found:
                    output.add(found)
                board[i][j] = None
                directions = [[i+1, j], [i,j+1], [i-1,j], [i,j-1]]
                for nextRow, nextCol in directions:
                    if 0<=nextRow<len(board) and 0<=nextCol<len(board[0]) and board[nextRow][nextCol] in root[letter]:
                        dfs(nextRow, nextCol, root[letter])
                board[i][j] = letter
                if not nextLevel:
                    root.pop(letter)

        myTrie = Trie()
        for word in words:
            myTrie.addWord(word) 
        output = set()

        rowNum = len(board)
        colNum = len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in myTrie.root:
                    dfs(i,j,  myTrie.root) 
        return output
        
            
