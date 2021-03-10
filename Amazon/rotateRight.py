# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        start = head
        # k = k%n
        n = 1
        while start.next:
            start = start.next
            n+=1
        start.next = head
        
        newTail = head
        for i in range(n-k%n-1):
            newTail = newTail.next
            
        output = newTail.next
        newTail.next = None
    
        return output
            
        
