# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #input
        #output
        #edge cases
        #constraints
        #brute force
        #approach and pattern:
        # time complexity:
        #space:
        if not root:
            return []

        q = deque() # contains list of per level nodes
        q.append([root])

        res = []

        


        while q:
            addtoq = []
            addtores = []

            currlevel = q.popleft()

            for node in currlevel:
                if node:
                    addtores.append(node.val)
                    addtoq.append(node.left)
                    addtoq.append(node.right)
                
            if len(addtoq)>0:
                q.append(addtoq)
            if len(addtores)>0:
                res.append(addtores)
            
        return res





        