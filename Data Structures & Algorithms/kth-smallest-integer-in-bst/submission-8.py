# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # print the bst in order, grab the kth value from the end

        order = []


        def traverse(self, root): #returns root val
            if root.left:
                traverse(self, root.left)
            order.append(root.val)
            if root.right:
                traverse(self, root.right)
            return root.val

        
        traverse(self, root)

        return order[k-1]

        