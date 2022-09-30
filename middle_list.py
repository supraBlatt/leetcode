# Definition for singly-linked list.
from decimal import HAVE_THREADS
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:

    ## naive approach using counting 
    #def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## get length 
        #count = 0
        #mover = head 
        #while mover: 
            #mover = mover.next
            #count += 1

        ## middle index
        #mover = head
        #mid_i = count // 2 

        ## advance to middle
        #count = 0
        #while count < mid_i: 
            #mover = mover.next 
            #count += 1
        
        #return mover 

    # a bit less naive using 2 pointers
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # fast head advances twice as fast 
        fast = slow = head 
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 
        return slow 
        # so no head? 
