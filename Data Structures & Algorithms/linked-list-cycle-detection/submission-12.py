# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next: #imp check for fast.next too bcz what if there is no cycle and fast.next == None. Then u cant do fast.next.next
            fast = fast.next.next
            slow = slow.next

            if slow==fast:
                return True
        return False