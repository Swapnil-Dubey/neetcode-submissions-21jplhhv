# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #to get the kth smallest value, we need in order traversal (to get ordered list of node values in the bst)
        self.arr = []
        self.dfs(root)
        return self.arr[k-1]

    def dfs(self, root):
        if root == None:
            return None
        
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)

        return root