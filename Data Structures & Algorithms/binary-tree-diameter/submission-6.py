# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#input: roof of tree
#output: diameter of tree
#constraints: 1 <= number of nodes in the tree <= 100
#            -100 <= Node.val <= 100
#pattern: Trees
#approach: Recursion on height + keeping a global variable res (max diameter seen until now) - dim is left+right height. Height is 1+max(left height ,right height)
#time complexity:O(n)
#space complexity:O(n)
        self.res = 0
        self.height(root)
        return self.res
    
    def height(self, root):
        if root== None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        self.res = max(self.res, left+right)

        return 1+max(left, right)
