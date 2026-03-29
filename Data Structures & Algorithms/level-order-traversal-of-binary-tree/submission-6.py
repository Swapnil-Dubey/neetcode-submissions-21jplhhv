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
        queue = [[root]]
        res = []

        while queue:
            addtores = []
            addtoqueue = []
            curr = queue.pop(0)
            for node in curr:
                addtores.append(node.val)
                if node.left:
                    addtoqueue.append(node.left)
                if node.right:
                    addtoqueue.append(node.right)
            if addtoqueue:
                queue.append(addtoqueue)
            res.append(addtores)
        return res


