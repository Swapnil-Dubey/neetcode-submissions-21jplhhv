# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first find halfway point

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None


        #head, head2
        
        #now reverse head2
        prev = None
        curr = head2
        next = head2

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head2 = prev

        #head2, head
        

        #now alternatively build result (IN PLACE no NEW NODES)
        res = head

        while head2:
            headrest = head.next
            head2rest = head2.next

            head.next = head2
            head2.next = headrest

            head = headrest
            head2 = head2rest





