# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #input: heads of 2 sorted LL
        #output:  head of new sorted combined LL
        #constraints: 0 <= The length of the each list <= 100.
        #approach: create a dummy node, pick lower value node from either lists and keep going until either or both of them is empty
        #edge cases: Length of either or both lists is 0
        #pattern: LL
        #time complexity: O(n+m)
        #space complexity: O(1) ***IMP CANT CREATE NEW NODES

        curr = ListNode() #Dummy node
        tail = curr

        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2


        
        return curr.next


        

