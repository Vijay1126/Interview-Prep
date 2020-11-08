class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = head =  ListNode(None)
        carry = 0
        
        while l1 or l2:
            firstVal = l1.val if l1 else 0
            secondVal = l2.val if l2 else 0
            currSum = firstVal+secondVal+carry
            carry, digit = divmod(currSum, 10)
    
            output.next = ListNode(digit)
            output = output.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry==1:
            output.next = ListNode(1)
        return head.next
            
            
