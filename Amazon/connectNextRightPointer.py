"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nextLevel = pointer = Node(0)
        head = root
        
        while head:
            while head:
                if head.left:
                    pointer.next = head.left
                    pointer = pointer.next
                if head.right:
                    pointer.next = head.right
                    pointer = pointer.next
                head = head.next
            head = nextLevel.next
            pointer = nextLevel
            pointer.next = None
        
        return root
        
        
