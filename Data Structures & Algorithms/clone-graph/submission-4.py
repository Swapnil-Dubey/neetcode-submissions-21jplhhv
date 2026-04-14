"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #return deep copy of the graph
        oldtonew = {}
        
        #generates new graph portion originating at node(old)
        def dfs(node):
            if not node:
                return None
            if node in oldtonew:
                return oldtonew[node]

            newnode = Node(node.val)
            oldtonew[node] = newnode
            for n in node.neighbors:
                copyneighbor = dfs(n)
                newnode.neighbors.append(copyneighbor)
            
            return newnode
        
        return dfs(node)