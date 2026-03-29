"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        res = dummy
        mapping = {}
        head2 = head
        while head:
            res.next = Node(head.val)
            mapping[head] = res.next
            head = head.next
            res = res.next
        
        res = dummy
        #res and head2

        while head2:
            res.next.random = mapping[head2.random] if head2.random else None
            head2 = head2.next
            res = res.next
        
        return dummy.next


        