# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#input: list 1, list 2 (heads of 2 sorted linked lists)
#output: head of new merged sorted linked list
#constraints:0 <= The length of the each list <= 100.
#             -100 <= Node.val <= 100

#edge cases: List 1 is None, List 2 is None
#pattern: Linked List
#approach:  
#time complexity: O(n+m)
#space complexity:O(1)
        if list1 == None:
            return list2
        elif list2 == None :
            return list1
        
        res = None
        
        while True:
            if res == None:
                if list1.val<list2.val:
                    res = list1
                    head = res
                    list1 = list1.next
                else:
                    res = list2
                    head = res
                    list2 = list2.next

            else:
                if list1!= None and list2!=None:
                    if list1.val<list2.val:
                        res.next=list1
                        list1 = list1.next
                    else:
                        res.next=list2
                        list2 = list2.next

                    res = res.next
                    
                else:
                    if list1==None:
                        res.next = list2
                        return head
                    else:
                        res.next = list1
                        return head
        return head
                