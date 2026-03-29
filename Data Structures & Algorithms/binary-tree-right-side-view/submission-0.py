# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #output = listof values of nodes visible from right side of the tree ordered top to bottom
        # constraints: 0 <= number of nodes in the tree <= 100

        #edge case: 0 nodes
        #approach: recursive (at each level append to the list the left node if there is no right node, and right node if there is a right node)

        if root == None: #EDGE CASE FOR EMPTY ROOT***
            return []

        queue = [[root]]
        res = []

        while queue:
            leveltosearch = queue[0]

            appendtoqueue = []


            for n in range(len(leveltosearch)):
                if n == len(leveltosearch)-1:
                    res.append(leveltosearch[n].val)
                if leveltosearch[n].left:
                    appendtoqueue.append(leveltosearch[n].left)
                if leveltosearch[n].right:
                    appendtoqueue.append(leveltosearch[n].right)

            queue.pop(0)
            if appendtoqueue: #IMPP: DONT ADD ENPTY LIST (LEAF NODE CASE)
                queue.append(appendtoqueue)
        return res



        