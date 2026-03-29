# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, currmax):
            if root == None:
                return self.res

            if currmax>root.val:
                dfs(root.left, currmax)
                dfs(root.right, currmax)
            else:
                self.res+=1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
        dfs(root, root.val)
        return self.res
            

