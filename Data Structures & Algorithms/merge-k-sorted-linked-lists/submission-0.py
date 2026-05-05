# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #input = list of list nodes (size k)
        #output = sorted LL 
        #constraints = 0 <= lists.length <= 1000
        #   0 <= lists[i].length <= 100
        #   -1000 <= lists[i][j] <= 1000

        #edge cases: len(lists) = 0, len(lists[0]) = 0, lists is None, lists is len 0

        # brute force: at each iteration, go through all linked lists, grab the smallest one and add to the end of res list, move it along on the original LL
        # pattern and approach: linked list, merge sort (take pairs of 2 from the k lists, merge 2 at a time) 
        # time complexity: O(nlogk) -> n is the time for merging 2 LL, and we do it log k times
        # space complexity: O(n)
        if lists == None or len(lists) == 0:
            return None

        while len(lists)>1:
            l1 = lists.pop()
            l2 = lists.pop()

            mergedList = self.mergeList(l1,l2)
            lists.append(mergedList)
        return mergedList



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


