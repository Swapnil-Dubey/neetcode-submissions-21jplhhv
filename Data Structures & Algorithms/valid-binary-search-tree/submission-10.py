# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #input= root of bst

    #output = true if valid bst

    #constraints:
    #brute force
    #pattern and approach:
    #edge cases: 
    #time copmlexity
    #space complexity

        return self.isValid(root.left,-float('inf'),root.val) and self.isValid(root.right,root.val,float('inf'))

    def isValid(self, root, leftmax, rightmax):
        if root == None:
            return True
        
        if not (leftmax<root.val<rightmax):
            print("left",leftmax)
            print("curr",root.val)
            print("right",rightmax)

            return False
        
        return self.isValid(root.left, leftmax,root.val) and self.isValid(root.right, root.val,rightmax)
