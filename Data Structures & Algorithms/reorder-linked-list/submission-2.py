# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None

        #head and head2
        #reorder head2

        prev = None
        curr = head2

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev

        #head1, head2
        head1 = head

        currh1 = head1
        currh2 = head2

        while currh1 and currh2:
            nexth1 = currh1.next
            currh1.next = currh2
            nexth2 = currh2.next
            currh2.next = nexth1
            currh1 = nexth1
            currh2 = nexth2
        if not head1 and not head2:
            return head1

        if not head1:
            currh1.next = currh2
        
