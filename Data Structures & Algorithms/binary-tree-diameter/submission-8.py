# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #constraints: Diam = length of longest path between any 2 nodes in the tree
        #           path doesnt have to pass through the root
        # output: diameter of the tree
        # 1<= no. of node sin the tree <= 100
        self.diameter = 0
        self.height(root)
        return self.diameter

    def height(self, root):
        if root == None:
            return 0

        self.diameter = max(self.diameter, self.height(root.left)+self.height(root.right))

        return 1+max(self.height(root.left), self.height(root.right))

    