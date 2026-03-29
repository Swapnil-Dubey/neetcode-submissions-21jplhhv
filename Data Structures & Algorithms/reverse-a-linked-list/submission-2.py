# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#input: head of LL
#output: head of reversed LL
#constraints:0 <= The length of the list <= 1000.
#edge cases:length of list = 0 or 1 or 2
#pattern:LL ( prev, curr, next nodes)

#time complexity:O(n)
#space complexity:O(1)
        prev = None
        curr = head
        next = head

        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev