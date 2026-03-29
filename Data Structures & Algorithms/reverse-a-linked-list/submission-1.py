# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#input: head(beginning) of a singly linked list
#output: new beginning of reversed linked list
#constraints: 0 <= The length of the list <= 1000.
#               -1000 <= Node.val <= 1000

#edge cases: length of list = 0, 1
#pattern: linked list
#approach: 3 pointer (prev, curr, next)
#time complexity: O(n)
#space complexity:O(1)
        prev = None
        curr = head


        if curr== None or curr.next == None:
            return curr

        next = None

        while curr!= None:
            next = curr.next
            curr.next = prev  
            prev = curr 
            curr = next
        return prev




        
            

