# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#input: head of LL and int n
#output: head of LL with nth node from end removed
#constraints: len(list) == sz, 1<=sz<=30, 1<=n<=sz
#edge cases: 1 element list, 2 element list (head removal)
#pattern: Linked list
#approach: make  2 pointers originated 1 at head and another at dist n from it then iterate through the LL
#          until the further ahead pointer reaches last node
#time complexity: O(n)
#space complexity:O(1)

        curr = head
        next = head
        prev = None


        for i in range(n):
            next = next.next


        if not next: # imp edge case here is that what if n=sz (n input param is eq to no. of elements in array)
            # that means the while loop below would never run!
            return head.next

        while next:
            prev = curr
            next = next.next
            curr = curr.next



        prev.next = curr.next
        curr.next = None


    
        return head
        
        
        
        