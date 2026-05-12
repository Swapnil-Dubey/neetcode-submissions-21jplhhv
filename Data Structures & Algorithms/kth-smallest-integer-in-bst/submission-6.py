# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ino = self.inorder(root, [])

        return ino[k-1]
    
    #return list (inorder traversal of bst)
    def inorder(self,root, inorder):
        if root == None:
            return inorder
        

        self.inorder(root.left,inorder)
        inorder.append(root.val)
        self.inorder(root.right,inorder)

        return inorder




