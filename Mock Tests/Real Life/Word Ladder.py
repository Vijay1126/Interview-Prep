class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        wordList = set(wordList)
        wordMap = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    tempWord = word[:i] + letter + word[i+1:]
                    if tempWord in wordList and tempWord!=word:
                        wordMap[word].append(tempWord)
                    
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            currWord, pathLength = queue.popleft()
            if currWord==endWord:
                return pathLength
            else:
                visited.add(currWord)
                for word in wordMap[currWord]:
                        queue.append((word,pathLength+1))
        
        return 0
                
                        
                
