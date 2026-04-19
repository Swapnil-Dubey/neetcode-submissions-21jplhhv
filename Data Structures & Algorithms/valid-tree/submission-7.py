class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree = n-1 edges where n is nodes and there are no cycles
        PARENTS = [i for i in range(n)]
        RANK = [1]*n

        if len(edges)!=n-1:
            return False

        def find(n):
            while n!=PARENTS[n]:
                n = PARENTS[PARENTS[n]]
            return n

        def union(n1,n2):
            parentn1 = find(n1)
            parentn2 = find(n2)

            if parentn1 == parentn2:
                return False

            if RANK[parentn1]>=RANK[parentn2]:
                PARENTS[parentn2] = parentn1
                RANK[parentn1]+=1
            else:
                PARENTS[parentn1] = parentn2
                RANK[parentn2]+=1
        
        for x,y in edges:
            ret = union(x,y)
            if ret == False:
                return False
        return True
            