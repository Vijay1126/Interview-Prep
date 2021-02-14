class Node:
    def __init__(self, key, value):
        self.value = value 
        self.key = key
        self.freq = 1
        self.next = None
        self.prev = None
    
class DLL:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        
    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.size+=1
            return 
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size+=1
        # print("Head", self.head.value, "tail", self.tail.value)
        return 

    def removeNode(self, node):
        if node == self.head and node == self.tail:
            # print("Head", self.head.value, "tail", self.tail.value)
            self.head = None
            self.tail = None
        elif node == self.head:
            print("Deleting head")
            nextNode = self.head.next
            nextNode.prev = None
            self.head.next = None
            self.head = nextNode
        elif node == self.tail:
            print("Deleting Tail")
            secondLastNode = self.tail.prev
            secondLastNode.next = None
            self.tail.prev = None
            self.tail = secondLastNode
        else:
            print("Deleting middle node")
            prev = node.prev
            nextNode = node.next
            prev.next = nextNode
            nextNode.prev = prev
        self.size-=1
            
            
    def removeTail(self):
        tail = self.tail 
        self.removeNode(tail)
        return tail
    
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(Node)
        self.freqMap = defaultdict(DLL)
        self.capacity = capacity
        self.size = 0
        self.currMin = 1

    def get(self, key: int) -> int:
        # print("Getting Key", key, self.freqMap)
        # print("Cache", self.cache)
        if key in self.cache:
            print("Present", self.cache[key].value, self.cache[key])
            node = self.cache[key]
            self.updateNodeFreq(node)
            print("Updated node count", node.freq, self.freqMap)
            return node.value
        else:
            return -1
        
    def updateNodeFreq(self, node):
        # print("Updating", node.value, self.freqMap)
        #get current frequency 
        currentFrequency = node.freq
        currMap = self.freqMap[currentFrequency]
        
        #remove it from the frequency map
        currMap.removeNode(node)
        
        #update curr min if needed
        if currMap.size == 0 and currentFrequency == self.currMin:
            self.currMin +=1
        node.freq+=1
        
        #insert into the map back
        self.freqMap[node.freq].setHead(node)
       
        
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        print("Putting", key)
        #check if already present
        if key in self.cache:
            print("Present")
            node = self.cache[key]
            node.value = value #update the value
            self.updateNodeFreq(node)
        
        #else
        else:
            print("Not Present")
            if self.size == self.capacity:
                print("Capacity reached")
                deletedNode = self.freqMap[self.currMin].removeTail()
                del self.cache[deletedNode.key]
                self.size-=1
            nodeToAdd = Node(key, value)
            self.cache[key] = nodeToAdd
            self.freqMap[1].setHead(nodeToAdd)
            self.currMin = 1
            self.size+=1
        
        #check for capacity

Time complexity: O(1)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
