# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #input: 2 linked lists (sorted individually)
        #output: head of new joined sorted linked list
        # constraints: length of list min = 0, max = 100 
        #               node val can be negative

        # approach: taken curr1 curr2(1 pointer each for curr psn on the linked lists). compare value attach the min one and move that respective curr pointer. while loop until either reaches end(null) of linked list

        # time complexity:O(n)
        # examples (run through): 


        #edge and normal cases: length of either or both lists = 0, unequal lengths, equal lengths, equal values



        head = ListNode()
        curr = head

        #list1
        #list2


        while list1 and list2:
            if list1.val<list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else: 
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return head.next