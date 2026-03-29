# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth = head
        end = head
        prev = None

        for i in range(n):
            end = end.next

        while end:
            end = end.next
            prev = nth #what if this never runs!! then prev wil lbe stuck at null
            nth = nth.next

        if prev==None: #head removal edge case
            return head.next
        prev.next = nth.next

        return head