# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#input: head of LL
#output: true if cycle in list
#brute force: hashset seen (O(n) space)
#edge cases: 0 length list, 1 lenght list
#pattern: LL
#approach: slow and fast pointer
#time complexity: O(n)
#space complexity: O(1)

        if head == None or head.next == None:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
    
        return False

            