class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        
        even = evenStart = head
        odd = oddStart = head.next
        
        while even.next and even.next.next:
            even.next = even.next.next
            even = even.next
            odd.next = even.next
            odd = odd.next
        even.next = oddStart
        return(evenStart)
