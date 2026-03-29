# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [[root]]
        res = []

        while queue:
            addtoqueue = []
            addtores = []

            level = queue[0]
            for n in level:
                addtores.append(n.val)
                if n.left:
                    addtoqueue.append(n.left) #imp : dont append if nleft isnone
                if n.right:
                    addtoqueue.append(n.right)#imp : dont append if nright isnone
            
            if addtoqueue:
                queue.append(addtoqueue) #imp : dont append if addtoqueue is empty
            res.append(addtores)
            queue.pop(0)
        return res
            
