# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head

        for i in range(n):
            second = second.next

        prev = None
        while second:       #this will not run only in n = len(head) case ( removing the head and return rest of the list)
            prev = first
            second = second.next
            first = first.next
        if prev == None:
            return head.next
        prev.next = first.next

        return head
        


        
