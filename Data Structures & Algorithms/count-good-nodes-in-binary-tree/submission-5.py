# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root, maxSeen):
        if root == None:
            return 0
        if root.val>=maxSeen:
            res = 1
            maxSeen = root.val
        else:
            res = 0
            

        return res+self.dfs(root.left, maxSeen)+self.dfs(root.right, maxSeen)