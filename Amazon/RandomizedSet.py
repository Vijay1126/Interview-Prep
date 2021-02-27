class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = defaultdict(int)
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.numbers:
            return False
        self.list.append(val)
        self.numbers[val] = len(self.list)-1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.numbers:
            index = self.numbers[val]
            #update the value in the dict 
            self.numbers[self.list[-1]] = index
            self.list[index], self.list[-1] = self.list[-1], self.list[index]
            self.list.pop()
            del self.numbers[val]
            
            

            return True
        return False
        
#          if(val not in self.hmap):
#             return False
#         index = self.hmap[val]
#         self.hmap[self.lists[-1]] = index
#         self.lists[index], self.lists[-1] = self.lists[-1], self.lists[index]
#         self.lists.pop()
#         self.hmap.pop(val)
#         self.length -= 1
#         return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return random.choice(self.list )

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
