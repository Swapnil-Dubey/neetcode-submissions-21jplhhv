# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        res = []
        queue = [[root]]
        

        while queue:
            currlvl = queue.pop()
            appendtoqueue = []
            for node in range(len(currlvl)):
                if node == len(currlvl)-1:
                    res.append(currlvl[node].val)
                if currlvl[node].left:
                    appendtoqueue.append(currlvl[node].left)
                if currlvl[node].right:
                    appendtoqueue.append(currlvl[node].right)
            if appendtoqueue:
                queue.append(appendtoqueue)
        return res

        