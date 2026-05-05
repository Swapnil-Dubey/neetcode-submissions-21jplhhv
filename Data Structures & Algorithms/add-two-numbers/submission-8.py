# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0


        while l1 or l2 or carry:
            currsum = 0
            if l1:
                currsum+=l1.val
                l1 = l1.next
            if l2:
                currsum+=l2.val
                l2 = l2.next
            currsum+=carry
            carry = 0

            if currsum>9:
                carry = currsum//10
                currsum = currsum%10
                

            head.next = ListNode(currsum)
            head = head.next
        return dummy.next
