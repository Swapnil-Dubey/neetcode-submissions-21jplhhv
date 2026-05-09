# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #level order traversal but only gonna add the rightmost value at current level into res
        res = []

        q = deque() #remember this***
        q.append([root])

        while q:
            currlevel = q.popleft()
            
            addtores = []
            addtoq = []

            for curr in currlevel:
                if curr:
                    addtores.append(curr.val)

                    if curr.left:
                        addtoq.append(curr.left)
                    if curr.right:
                        addtoq.append(curr.right)
            if len(addtores)>0:
                res.append(addtores[-1])
            if len(addtoq)>0:
                q.append(addtoq)
        return res
                



