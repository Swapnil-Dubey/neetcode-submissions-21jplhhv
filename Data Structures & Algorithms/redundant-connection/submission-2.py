class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        PARENTS = [i for i in range(n+1)]
        RANK = [1]*(n+1)


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
            print(x,y)
            res = union(x,y)
            if res == False:
                return [x,y]