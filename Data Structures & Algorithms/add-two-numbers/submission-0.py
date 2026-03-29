# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0
    

        while l1 or l2 or (carry!=0):

            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
                
            currsum = v1+v2+carry

            carry = 0

            if currsum>=10:
                carry = currsum//10
                currsum = currsum%10
            
            curr.next = ListNode(currsum)
            curr = curr.next # dont forget


            if l1:
                l1=l1.next
            
            if l2:
                l2 = l2.next

        return dummy.next


