class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #graph is a tree when nodes = n, edges = n-1 and no cycles

        rank = [0]*n
        parent = [i for i in range(n)]

        if len(edges)!=n-1:
            return False






        # return parent of nth node in the graph
        def find(n):
            while n!=parent[n]:
                n = parent[parent[n]]
            return n


        def union(n1,n2):

            parentn1 = find(n1)
            parentn2 = find(n2)

            if parentn1 == parentn2:
                return False
            

            if rank[parentn1]>=rank[parentn2]:
                parent[parentn2]=parentn1
                rank[parentn2]+=1
            else:
                parent[parentn1]=parentn2
                rank[parentn1]+=1
            return True
        

        for (n1,n2) in edges:
            res = union(n1,n2)
            if res == False:
                return False
        

        return True
        
        

