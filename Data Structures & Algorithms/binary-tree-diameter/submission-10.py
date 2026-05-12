# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #ca;culate height of left subtree and height of right subtree at each node, return the max
        return self.helper(root,0)



    def height(self,root):
        if root == None:
            return 0

        return 1+max(self.height(root.left),self.height(root.right))


    def helper(self,root,res):
        if root == None:
            return res
        if self.height(root.left)+self.height(root.right)>res:
            res = self.height(root.left)+self.height(root.right)
        return max(res,self.helper(root.left, res),self.helper(root.right, res))


