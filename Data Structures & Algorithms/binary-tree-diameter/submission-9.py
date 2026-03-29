# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0

        self.height(root)
        return self.diam

    def height(self, root):
        if root == None:
            return 0
        
        self.diam = max(self.diam, self.height(root.left) + self.height(root.right))
        
        return 1+max(self.height(root.left), self.height(root.right))

    