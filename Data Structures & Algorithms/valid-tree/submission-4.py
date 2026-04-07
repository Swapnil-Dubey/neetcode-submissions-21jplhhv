class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #input = n nodes, list of edges (ai, bi)
        #output = true if valid tree
        #constraints: no duplicate edges (ai,bi) = (bi,ai)
        #   1 <= n <= 100
        #   0 <= edges.length <= n * (n - 1) / 2
        #pattern: graphs
        #approach: check for cycle, if it exists then its not a valid tree, using union find
        #edge cases:1 node 0 edges, 2 nodes 0 edges
        #time complexity:
        #space complexity:


        #no cycles and n-1 edges to be a tree.

        if len(edges)!=n-1:
            return False

        parent = [i for i in range(n)]
        rank = [1]*n


        def parents(n):
            while n!=parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n
    
        def union(n1, n2):
            parentn1 = parents(n1)
            parentn2 = parents(n2)

            if parentn1== parentn2:
                return 0
            
            if rank[parentn1] >= rank[parentn2]:
                parent[parentn2] = parentn1
                rank[parentn1]+=1
            else:
                parent[parentn1] = parentn2
                rank[parentn2]+=1
            return 1
        
        for (a,b) in edges:
            ret = union(a,b)

            if ret == 0:
                return False
        return True
        






