class FileSystem: 
    def __init__(self):
        self.myTrie = Trie()

    def ls(self, path: str) -> List[str]:
        return self.myTrie.getAllFiles(path)

    def mkdir(self, path: str) -> None:
        self.myTrie.makeDir(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.myTrie.addContent(filePath, content)

    def readContentFromFile(self, filePath: str) -> str:
        return self.myTrie.readContent(filePath)
class Trie:
    def __init__(self):
        self.start = {}
        
        
    def makeDir(self, path):
        path = path.split("/") # => [ a, b, c]
        print("Making", path)
        start = self.start 
        
        for item in path:
            if item:
                if item not in start:
                    start[item] = {}
                start = start[item]
        return 
    
    def addContent(self, path, content):
        print("Adding")
        path = path.split("/")
        start = self.start 
        lastItem = None
        for item in path:
            if item:
                if item not in start:
                    start[item] = {}
                start = start[item]                
                lastItem = item
        # start[1] = 1
        # start["content"] = [] 
        print(self.start, start, content)
        if "content" in start:
            print("old", start["content"], content)
            start["content"]= start["content"]+content
        else:
            start["content"] = content
            
        return 
                

    def getAllFiles(self, path):
        path = path.split("/") # => [ a, b, c]
        # print(newPath)
        start = self.start
        for item in path[1:]:
            if item:
                print(item)
                if item in start:
                    start = start[item]
                else:
                    print("Wait, what?")
        print(start)
        if "content" in start:#file path,return file name
            print("first")
            # print(newPath[-1])
            return [path[-1]]
        else:
            print("Second")
            allFiles = []
            return sorted([i for i in start])
    def readContent(self, path):
        path = path.split("/")
        start = self.start 
        for item in path:
            if item:
                if item not in start:
                    print("What the..")
                start = start[item]
        print(start, path, self.start)
        return start["content"]
        
        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
