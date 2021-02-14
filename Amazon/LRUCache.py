#This is our doubly linked list node 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
#Doubly linked list class
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.capacity = 0
    
    
    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.updateHead(self.head, node)
        self.capacity+=1
        return
    
    def updateHead(self, node, addNode):
        #None -> 5 -> 1 -> 2 -> 3 //ADD 5 - > 1
        #None ->    Head
        if node == self.head:
            #prev of node will be None cause it is the start
            #in this question it will always be
            addNode.next = self.head
            self.head.prev = addNode
            self.head = addNode
        return self.head
    
    def removeTail(self):
        deletedNodeKey = self.tail
        self.removeNode(self.tail)
        # print("Deleting", deletedNodeKey.value)
        return deletedNodeKey.value
    
    def removeNode(self, node):
        #None -> 5 -> 1 -> 2 -> 3 //ADD 5 - > 1
        # Node can be the tail
        if node == self.tail and node == self.head:
            self.head = self.tail = None
        elif node == self.tail:
            secondLastNode = self.tail.prev
            secondLastNode.next = None
            self.tail.prev = None
            self.tail = secondLastNode
        # Node can be the head
        elif node == self.head:
            secondNode = self.head.next
            secondNode.prev = None
            self.head.next = None
            self.head = secondNode
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode

        self.capacity-=1
        return 
    def getHead(self):
        return self.head
    
    
            
class LRUCache:
    def __init__(self, capacity: int):
        #Hashmap to see if we have it and to store the value of the key 
        self.hashmap = {}
        self.DLL = DLL()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        # print("Getting", key, self.hashmap, "Current head",self.DLL.head.value, "Current Tail",self.DLL.tail.value)
        if key in self.hashmap:
            #Get the value
            
            node, val = self.hashmap[key]
            #Remove the Node and delete it from the hashmap
            self.DLL.removeNode(node)    
            # del self.hashmap[key]
            #Add it as the new head
            self.DLL.setHead(node)
            #Return the value
            # print("After Getting", key, "New Head",self.DLL.head.value,"New Tail", self.DLL.tail.value)
            return val 
        else:
            # print("No key to get")
            return -1

    
    def put(self, key: int, value: int) -> None:
        # print("Putting", key , value, self.hashmap)
        #capacity
        #if capacity is less than our allotted capacity:
        newNode = Node(key)
        if key in self.hashmap:
            # print("Key found")
            self.DLL.removeNode(self.hashmap[key][0])
            self.hashmap[key] = [newNode,value]
            self.DLL.setHead(newNode)
        else:                
            # print("Key not found")
            if self.capacity == self.DLL.capacity:
                # print("Capacity reached", self.hashmap)
                deletedNodeKey = self.DLL.removeTail()
                del self.hashmap[deletedNodeKey]
            self.DLL.setHead(newNode)
            self.hashmap[key] = [newNode, value]
        # print("After putting", key , self.hashmap, "New head", self.DLL.head.value, "New Tail", self.DLL.tail.value)
                
            
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
