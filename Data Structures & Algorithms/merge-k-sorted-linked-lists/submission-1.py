# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #take 2 lists at a time, keep merging them until u have just 1 list left
        if not lists or len(lists) == 0:
            return None

        while len(lists)>1:
            l1 = lists.pop()
            l2 = lists.pop()

            lists.append(self.mergeList(l1,l2))
        return lists[0]
    

    def mergeList(self, l1, l2):
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val>=l2.val:
                head.next = l2
                head = head.next
                l2 = l2.next
            else:
                head.next = l1
                head = head.next
                l1 = l1.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return dummy.next
