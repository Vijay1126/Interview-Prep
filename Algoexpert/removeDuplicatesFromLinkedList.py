# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    root = linkedList
	if not root or not root.next:
		return root
	prev = root
	curr = root
	
	while curr:
		while curr and curr.value == prev.value:
			curr = curr.next
		prev.next = curr
		prev = curr

		
	return root
		
		
	
