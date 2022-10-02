# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # inital sketch
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # my basic idea was to add both nodes and the carry. and then update the carry 
        # run as long as either of the lists still goes on, or the carry does 
        # has a lot of redundant computations
        head1, head2 = l1, l2
        carry = 0
        result = ListNode()
        cur = result
        
        # oh my god this is a mess of Promise checking
        while head1 or head2 or carry: 
            
            # calculate and update carry 
            val1 = 0 if (not head1) else head1.val
            val2 = 0 if (not head2) else head2.val
            res = val1 + val2 + carry
            carry = res//10
            cur.next = ListNode(res%10)

            cur = cur.next
            head1 = None if not head1 else head1.next
            head2 = None if not head2 else head2.next

        # crafted a redundant first node. check if it can be removed        
        if result.next: 
            return result.next
        return result
            
        