# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0

        while l1 or l2 or carry: # dont forget that carry can be non empty even if lists are empty
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            currsum = l1.val + l2.val +carry
            carry= 0# remember this is essential
            currdig = currsum%10
            carry = currsum//10

            res.next = ListNode(currdig)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        return dummy.next
        


        