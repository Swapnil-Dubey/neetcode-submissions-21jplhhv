# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None


        #head,head2

        #reverse head2 list
        prev = None
        curr = head2
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr= next

        head2 = prev

        #head, head2. now alternatively join the two lists

        mainhead = head

        while head and head2:
            curr1 = head.next
            head.next = head2
            head = head.next
            curr2 = head2.next
            head.next = curr1
            head = head.next
            head2 = curr2





