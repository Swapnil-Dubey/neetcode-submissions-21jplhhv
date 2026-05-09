# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append([root])
        res = []

        while q:
            
            currentlevel = []
            currentleveladdtoqueue = []
            currlevel = q.popleft()
            for curr in currlevel:
                if curr:
                    currentlevel.append(curr.val)
                    if curr.left:
                        currentleveladdtoqueue.append(curr.left)
                    if curr.right:
                        currentleveladdtoqueue.append(curr.right)
            if len(currentlevel)>0:
                res.append(currentlevel)
            if len(currentleveladdtoqueue)>0:
                q.append(currentleveladdtoqueue)
        return res
