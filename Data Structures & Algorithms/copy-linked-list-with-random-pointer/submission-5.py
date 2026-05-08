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

        dummy = Node(0)
        head_new = dummy
        orig = head



        while head:
            head_new.next = Node(head.val)
            oldtonew[head] = head_new.next
            head = head.next
            head_new = head_new.next

        head = orig
        head_new = dummy.next

        while head:
            if head.random:
                head_new.random = oldtonew[head.random]
            head =head.next
            head_new = head_new.next
        return dummy.next
        
            
