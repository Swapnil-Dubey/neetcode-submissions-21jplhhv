# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head1 = head
        head2 = head

        while head2 and head2.next:
            head1 = head1.next
            head2 = head2.next.next

        head2 = head1.next
        head1.next = None

        head1 = head

        #head1, head2

        prev = None
        curr = head2
        
        while curr:
            next = curr.next
            curr.next= prev
            prev = curr
            curr = next

        head2 = prev

        #head1, head2

        while head1 and head2:
            h1next = head1.next
            h2next = head2.next

            head1.next = head2
            head2.next = h1next
            head1 = h1next
            head2 = h2next
        
