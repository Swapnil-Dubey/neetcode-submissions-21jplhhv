class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # input: graph of n nodes, array edges
        # output: number of connected components in the graph
        # constraints:1 <= n <= 2000
                        #1 <= edges.length <= 5000
                        #edges[i].length == 2
                        #0 <= aᵢ <= bᵢ < n
                        #aᵢ != bᵢ
                        #There are no repeated edges
        #pattern: graphs
        #approach:
        #edge cases
        #time complexity:
        #space complexity:

        parent = [i for i in range(n)]
        rank = [1]*n

        #find root parent
        def find(node):
            res = node

            while res!=parent[res]:
                parent[res] = parent[parent[res]]#but if we dont have a grand parent wouldnt this cause issues
                res = parent[res]
            return res
        
        def union(node1, node2):
            rootparent1,rootparent2 = find(node1),find(node2)
            if rootparent1==rootparent2:
                return 0
            
            if rank[rootparent2]>=rank[rootparent1]:
                parent[rootparent1] = rootparent2
                rank[rootparent2] +=1
            else:
                parent[rootparent2] = rootparent1
                rank[rootparent1]+=1
            return 1
    
        res = n
        for n1,n2 in edges:
            res -= union(n1, n2)
        return res




        