# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root,root.val)
        return self.res
    

    def helper(self,root,maxseenuntilnow):
        if root == None:
            return
        if maxseenuntilnow<=root.val:
            self.res+=1
        
        maxseenuntilnow = max(root.val,maxseenuntilnow)
            
        self.helper(root.left, maxseenuntilnow)
        self.helper(root.right, maxseenuntilnow)