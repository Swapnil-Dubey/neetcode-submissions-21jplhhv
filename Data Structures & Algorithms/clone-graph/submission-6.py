"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # run dfs on node then on all its neighbors


        oldtonew = {}

        if node == None:
            return None



        def dfs(n):
            if n in oldtonew:
                return oldtonew[n]
            


            oldtonew[n] = Node(n.val)
            for i in n.neighbors:
                oldtonew[n].neighbors.append(dfs(i))
            
            return oldtonew[n]

        

        newNode = dfs(node)
        

        return newNode
    

    
