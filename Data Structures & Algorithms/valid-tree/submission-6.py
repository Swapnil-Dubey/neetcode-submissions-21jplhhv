class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is no. of edges = no.of nodes - 1 and no cycles 

        if n-1 != len(edges):
            return False
        

        #check cycles (union parent method)
        
        PARENTS = [i for i in range(n)]
        RANK = [1]*n


        def parent(n):
            while PARENTS[n]!=n:
                n = PARENTS[PARENTS[n]]
            return n
        
        def union(n1,n2):
            if parent(n1) == parent(n2):
                return False
            
            if RANK[parent(n1)]>=RANK[parent(n2)]:
                PARENTS[parent(n2)] = parent(n1)
                RANK[parent(n1)]+=1
            else:
                PARENTS[parent(n1)] = parent(n2)
                RANK[parent(n2)]+=1
        
        for (x,y) in edges:
            res = union(x,y)
            if res == False:
                return False
        return True

