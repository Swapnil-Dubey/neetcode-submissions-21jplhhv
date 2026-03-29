# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -1001, 1001)
    
    def helper(self, root, leftmax, rightmax):
        if root == None:
            return True
        
        if not leftmax<root.val<rightmax:
            return False
        
        return self.helper(root.left, leftmax, root.val) and self.helper(root.right, root.val, rightmax)
        

        