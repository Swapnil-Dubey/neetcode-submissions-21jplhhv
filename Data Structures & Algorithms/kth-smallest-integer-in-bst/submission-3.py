# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder traversal of a BST produces list of elements in order

        self.inorder = []
        

        def inorder(root):
            if root == None:
                return
            
            inorder(root.left)
            self.inorder.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return self.inorder[k-1]
        
        

            
