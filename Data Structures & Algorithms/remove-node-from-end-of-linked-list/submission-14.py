# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        end = head
        prev = head



        for i in range(n):
            end = end.next

        if not end:
            return head.next #.     imp edge case of what if n == len(linkedlist)

        while end:
            prev = curr
            curr = curr.next
            end = end.next
        prev.next = curr.next

        return head
        
        