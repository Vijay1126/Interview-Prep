# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.first = Heap(MAX_HEAP)
		self.second = Heap(MIN_HEAP)
		self.median = None
		
    def insert(self, number):
		if len(self.first.heap)==0 or number<self.first.peek():
			self.first.insert(number)
		else:
			self.second.insert(number)
		self.rebalanceHeaps(self.first, self.second)
		self.updateMedian()
	
	def updateMedian(self):
		first = self.first.heap
		second = self.second.heap
		if len(first) == len(second):
			print("1", self.first.peek())
			print("2", self.second.peek())
			self.median = (self.first.peek()+self.second.peek())/2
		elif len(first)-len(second) == 1:
			self.median = self.first.peek()
		else:
			self.median = self.second.peek()
		print("First",self.first.heap)
		print("Second", self.second.heap)
		
	def rebalanceHeaps(self, first, second):
		diff = len(first.heap)-len(second.heap)
		if diff == 2:
			second.insert(first.remove())
		elif diff == -2:
			first.insert(second.remove())
    def getMedian(self):
		print("Median Call", self.median)
        return self.median
def MAX_HEAP (a, b):
	return a>b
def MIN_HEAP(a,b):
	return a<b
class Heap:
	def __init__(self, comparator):
		self.comparator = comparator
		self.heap = []
	def insert(self, value):
		self.heap.append(value)
		self.siftUp(self.heap, len(self.heap)-1)
	def siftUp(self, array, currIndex):
		currParent = (currIndex-1)//2
		while currIndex>0:
			if self.comparator(array[currIndex], array[currParent]):
				self.swap(array, currIndex, currParent)
				currIndex = currParent
				currParent = (currIndex-1)//2
			else:
				return 
	def siftDown(self, array, currIndex):
		leftChild = currIndex*2+1
		while leftChild<len(array):
			rightChild = currIndex*2+2 if currIndex*2+2<len(array) else -1
			if rightChild!=-1 and self.comparator(array[rightChild],array[leftChild]):
				swapIndex = rightChild
			else:
				swapIndex = leftChild
			if self.comparator(array[swapIndex],array[currIndex]):
				self.swap(array, swapIndex, currIndex)
				currIndex = swapIndex
				leftChild = currIndex*2+1
			else:
				return 
		
	def peek(self):
		return self.heap[0]
	def remove(self):
		self.swap(self.heap, 0, len(self.heap)-1)
		value = self.heap.pop()
		self.siftDown(self.heap, 0)
		return value
	
	def swap(self, array, first, second):
		array[first], array[second] = array[second], array[first]
		
		
	
		
