# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # input = head of LL, int n
        #output = head of updated LL
        #constraints: number of nodes in  list is sz
        #   1<=sz<=30
        #   1<=n<=sz

        #Pattern: Linked list and two pointers

        #approach: initiate the 2 pointers at a dist of n from each other
        #   then iterate them 1 by 1 until the further pointer reaches None (end of list) then the pos of prev pointer is the
        #   position of the node u want to remove
        #time compl: o(n)
        #space: o(1)
                    #           imppp handle edge case of sz = n = 1 here
        left = head
        right = head
        prevLeft = None 

        for i in range(n):
            right = right.next

        
        while right:
            prevLeft = left
            left = left.next
            right = right.next

        if not prevLeft:
            return head.next #Summary TableScenarioDid while loop run?Value of prevLeftAction$n < sz$ (Middle/End)YesA NodeLink prev to left.next$n = sz$ (Head)NoNoneReturn head.next
            
        prevLeft.next = left.next
        left = None

        return head

        