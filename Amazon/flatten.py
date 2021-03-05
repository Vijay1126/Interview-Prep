"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def (self, head: 'Node') -> 'Node':
        if not head:
            return head
        start = head
        stack = [head]
            
        while True:
            start = stack.pop()
            while start.next or start.child:
                if start.child:
                    if start.next:
                        stack.append(start.next)
                    start.next = start.child
                    start.child.prev = start
                    start.child = None
                start = start.next
            if stack:
                start.next = stack[-1]
                stack[-1].prev = start
            else:
                break
        h = head
        while h:
            # print(h.child, h.val, h.next)
            h = h.next
        return head
            
