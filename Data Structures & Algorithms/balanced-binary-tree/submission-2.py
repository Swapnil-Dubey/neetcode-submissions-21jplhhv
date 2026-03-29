# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # contraints: no. of nodes in the tree -> [0,1000]
        # pattern: trees
        # approach: recursive approach, need a height helper function
        #time complexity: 

        if root == None:
            return True

        if abs(self.height(root.left)-self.height(root.right))>1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)



    def height(self, root1):
        if root1 == None:
            return 0
        

        return 1+max(self.height(root1.left), self.height(root1.right))