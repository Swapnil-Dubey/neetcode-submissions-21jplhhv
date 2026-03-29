# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #watch video
        if root == None:
            return []
        queue = [[root]]
        res = []

        while queue:
            listofnodesatlevel = queue[0]
            nextinqueue = []
            nextinres = []
            for node in listofnodesatlevel:
                if node:
                    nextinres.append(node.val)
                    nextinqueue.append(node.left)
                    nextinqueue.append(node.right)

            if nextinqueue:
                queue.append(nextinqueue)
            if nextinres:
                res.append(nextinres)
            queue.pop(0)
    



            
        return res
