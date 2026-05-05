# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #find the node such that node.left contains p and node.right contains q
        #       edge case what if that is never the case( p and q are part of the same branch)
        if root == None:
            return root
        if (self.isintree(root.left, p) and self.isintree(root.right,q)) or (root==p) or (root == q) or (self.isintree(root.left, q) and self.isintree(root.right,p)):
            return root
        if (self.lowestCommonAncestor(root.left, p, q)):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

    
    #return true if p is in root or not
    def isintree(self, root, p):
        if root == None:
            return False
        if root==p:
            return True
        return self.isintree(root.left, p) or self.isintree(root.right, p)


