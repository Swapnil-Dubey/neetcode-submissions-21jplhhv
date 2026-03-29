# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        #form inorder traversal in res
        self.helper(root)
        return self.res[k-1]
    
    def helper(self, root):
        if root == None:
            return None
        
        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)

        