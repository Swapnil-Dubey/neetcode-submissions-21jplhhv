# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #input LL l1, LL l2 (both non empty, non negative)
        #output = New LL sum of l1+l2
        # constraints: min length of l1 or l2 = 1
        # edge cases: example 2
        # approach and pattern: create a carry variable, that stores carry of curr sum of l1 and l2 
        dummynode = ListNode()
        curr = dummynode
        carry = 0
        while l1 or l2 or carry:
            currsum = 0

            if l1:
                currsum+=l1.val
            if l2:
                currsum += l2.val
                
            currsum += carry
            carry = 0

            if currsum>9:
                carry = currsum//10
                currsum = currsum%10
            curr.next = ListNode(currsum)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        return dummynode.next

            


            
