# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs but pick only rightmost element in the level to append to res

        res = []
        queue = [[root]]
        if root == None:
            return []
        
        

        while queue:
            appendtoqueue = []
            currlevel = queue.pop(0)

            for tn in range(len(currlevel)):
                if tn == len(currlevel)-1:
                    res.append(currlevel[tn].val)
                if currlevel[tn].left:
                    appendtoqueue.append(currlevel[tn].left)
                if currlevel[tn].right:
                    appendtoqueue.append(currlevel[tn].right)
            if appendtoqueue:
                queue.append(appendtoqueue)
        return res

