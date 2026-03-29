# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currlowest = None
        while root:
            currlowest = root
            if p.val<=root.val<=q.val or q.val<=root.val<=p.val:
                return currlowest
            
            elif root.val<=p.val:
                root = root.right
            else:
                root = root.left
            

