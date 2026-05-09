# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid
        #split the list
        #reverse the second list
        #join alternatively

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #now slow is at mid
        list2 = slow.next
        slow.next = None
        list1 = head

        #reverse list2
        prev = None
        curr = list2
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        list2 = prev
        head = list1
        
        while list1 and list2:
            l1next = list1.next
            l2next = list2.next

            list1.next = list2
            list2.next = l1next
            list1 = l1next
            list2 = l2next



