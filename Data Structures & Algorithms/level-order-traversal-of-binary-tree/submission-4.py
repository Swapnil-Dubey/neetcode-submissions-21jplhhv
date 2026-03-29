# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        res = []
        queue = [[root]]
        

        while queue:
            currlvl = queue.pop()
            appendtoqueue = []
            appendtores = []
            for node in currlvl:
                appendtores.append(node.val)
                if node.left:
                    appendtoqueue.append(node.left)
                if node.right:
                    appendtoqueue.append(node.right)
            if appendtores:
                res.append(appendtores)
            if appendtoqueue:
                queue.append(appendtoqueue)
        return res



