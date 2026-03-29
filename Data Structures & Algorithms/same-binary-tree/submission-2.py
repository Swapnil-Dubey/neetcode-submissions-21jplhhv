# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #constraints: Equivalent means structure and value of nodes is same
        #             0<= number of nodes in both trees <= 100
        #             -100 <= Node.val <= 100

        # output:  True if trees are equivalent
        # pattern: Trees
        # approach: at each pair of respective node, check if either is none (while both are not none) and then check for value
        #           equivalency, recursive approach on children
        # time complexity: O(n+m)
        # space complexity: O(1)

        if p==None and q==None:
            return True
        
        if p==None or q==None:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



        