# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      

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