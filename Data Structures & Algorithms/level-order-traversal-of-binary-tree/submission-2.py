# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #output: level order traversal (BFS) on a tree as a nested list (each list is a level L->R)
        #constraints: 0<= no. of nodes in the tree <= 1000

        #approach: use a queue (list), once you reach a parent, append its children nodes from L->r (as a list) into the queue and pop the parent 
        #          from the queue

        #time complexity: O(n)
        #space complexity: O(n)

        if root == None: #EDGE CASE FOR EMPTY ROOT***
            return []

        queue = [[root]]
        res = []

        while queue:
            leveltosearch = queue[0]

            appendtoqueue = []
            appendtores = []

            for n in leveltosearch:
                appendtores.append(n.val)
                if n.left:
                    appendtoqueue.append(n.left)
                if n.right:
                    appendtoqueue.append(n.right)

            queue.pop(0)
            if appendtoqueue: #IMPP: DONT ADD ENPTY LIST (LEAF NODE CASE)
                queue.append(appendtoqueue)
            res.append(appendtores)
        return res

