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
        dummy = Node(0)
        res = dummy
        oldtonew = {}

        head2 = head

        while head2:
            res.next = Node(head2.val)
            oldtonew[head2] = res.next
            res = res.next
            head2 = head2.next
        res=dummy.next
        
        while head:
            if head.random:
                res.random = oldtonew[head.random] #remember just one edge case where the original list node doesnt have a random node
            res = res.next
            head = head.next
        return dummy.next