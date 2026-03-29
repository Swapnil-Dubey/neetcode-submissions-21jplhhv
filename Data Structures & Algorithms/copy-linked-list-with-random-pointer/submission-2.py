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
        oldtonew = {}
        dummy = Node(-1)
        res = dummy

        head2 = head

        while head2:
            res.next = Node(head2.val)
            oldtonew[head2] = res.next

            head2 = head2.next
            res = res.next

        res = dummy.next

        while res:
            if head.random: #edge case: what if head.random is None
                res.random = oldtonew[head.random] 
            head = head.next
            res = res.next

        return dummy.next
        
