# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #input = root of binary tree
        #output = true if its valid BST
        #constraints:The left subtree of every node contains only nodes with keys less than the node's key.
        #            The right subtree of every node contains only nodes with keys greater than the node's key.
        #            Both the left and right subtrees are also binary search trees.
        #            1 <= The number of nodes in the tree <= 1000.
        # approach: helper function with max left and max right params
        #time complexity: O(n)
        #space: O(1)
        return self.helper(root, -1001, 1001)

    def helper(self, root, maxleft, maxright):
        if root == None:
            return True

        if not maxleft<root.val<maxright:
            return False
        
        return self.helper(root.left, maxleft, root.val) and self.helper(root.right, root.val, maxright)
            