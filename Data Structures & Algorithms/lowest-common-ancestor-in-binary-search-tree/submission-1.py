# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #input: root node, p node of root, q node of root
        #output: LCA of two nodes
        #constraints: all node values are unique
                    # 2 <= The number of nodes in the tree <= 100.
                    # -100 <= Node.val <= 100
                    # p != q
                    # p and q will both exist in the BST.
        #edge cases:number of nodes in tree = 2
        #pattern: Trees
        #approach: Binary search tree property
        #time complexity: O(h)
        #space complexity: O(1)

        while True:
            if p.val<=root.val<=q.val or q.val<=root.val<=p.val or root==p or root==q:
                return root
            elif root.val<=p.val:
                root = root.right
            else:
                root = root.left
        return -1