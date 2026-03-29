# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #every time you visit a node, look at its children and swap them

        # 1 base case
        if root is None:
            return None
        
        # 2 perform operation on root
        left = root.left
        root.left = root.right
        root.right = left

        #recursively perform operation on left and right subtrees of root (trust the natural recursion)
        self.invertTree(root.left)
        self.invertTree(root.right)

        # 3 return result at root
        return root