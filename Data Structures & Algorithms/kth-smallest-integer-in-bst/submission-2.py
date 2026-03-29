# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in order traversal of a bst produced list of ints in order
        self.inorder = []
        self.helper(root)
        return self.inorder[k-1]


    def helper(self, root):
        if root == None:
            return self.inorder
        self.helper(root.left)
        self.inorder.append(root.val)
        self.helper(root.right)