# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #output = number of good nodes
        #constraints: good node if path from root to that node has no 
        #             values greater than value of x
        # 1 <= number of nodes in the tree <= 100
        # -100 <= Node.val <= 100
        return self.dfs(root, root.val)

        
    def dfs(self, root2, currmax):
        if root2 == None:
            return 0
        if root2.val<currmax:
            res = 0
        else:
            res = 1
            currmax = max(currmax, root2.val)
        res+=self.dfs(root2.left, currmax)
        res+=self.dfs(root2.right, currmax)
        return res

        

        
