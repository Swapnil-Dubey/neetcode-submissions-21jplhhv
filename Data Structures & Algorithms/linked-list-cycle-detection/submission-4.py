# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast!=None and fast.next != None:# remember to think what will happen if there is NOT a cycle, then the fast pointer 
        #       or its next pointer will reach None !! (have to check for next too bcz below this we do .next.next)
            slow = slow.next
            fast = fast.next.next # have to first do .next on both slow and fast before checking == bcz at head they are both ==
                                    # cant really do (... and slow!= head) bcz what if the cycle is at head

            if slow == fast:
                return True;
        return False
