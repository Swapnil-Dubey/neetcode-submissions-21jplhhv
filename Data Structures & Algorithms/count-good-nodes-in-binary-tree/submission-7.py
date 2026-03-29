# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root,root.val)
    
    def helper(self, root, currmax):
        if root == None:
            return 0

        if root.val>=currmax:
            return 1+self.helper(root.left, root.val)+self.helper(root.right, root.val)  
        else:
            return self.helper(root.left, currmax)+self.helper(root.right, currmax) 
