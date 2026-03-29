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
        mapping = {}
        dummy = Node(0)
        res = dummy
        head2 = head
        while head2:
            res.next = Node(head2.val)
            mapping[head2] = res.next
            head2 = head2.next
            res = res.next
        
        head2 = head
        res = dummy.next
        while head2:
            if head2.random:
                res.random = mapping[head2.random]
            head2 = head2.next
            res = res.next
        
        return dummy.next


            