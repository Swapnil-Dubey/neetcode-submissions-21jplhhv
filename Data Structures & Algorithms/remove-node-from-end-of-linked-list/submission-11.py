# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        next = head
        prev = None

        for i in range(n):
            next = next.next

        while next:
            prev = curr
            curr = curr.next
            next = next.next
        if prev == None:
            return head.next
        prev.next = curr.next

        
        return head

        