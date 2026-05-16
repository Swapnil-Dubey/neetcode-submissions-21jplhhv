# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        #negative nodes edge case
        # at each node during a path, we have to take a split decision
        #brute: for everynode consider it to be the top most node and try to find from left subtree
            #what is the max sum we can create if we never split (basically including left and right subtrees both)
        

        #optimal: we do two things within the helper: updating res (max path that passes through n)
        #           and second is return the maxpath that passes through parent
        #O(n)
        #space = O(h) = logn if balanced tree



        res = float("-inf")


        def maxpathsum(n):
            nonlocal res
            if n == None:
                return 0
            

            left = max(0,maxpathsum(n.left))
            right = max(0,maxpathsum(n.right))

            res = max(res,n.val+left+right)

            return n.val+max(left,right)
        

        maxpathsum(root)
        return res
        
        

