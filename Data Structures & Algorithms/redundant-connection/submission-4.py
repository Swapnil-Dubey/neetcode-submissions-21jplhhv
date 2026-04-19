class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        PARENTS = [i for i in range(n+1)]
        RANK = [1]*(n+1)


        def find(n):
            while n!=PARENTS[n]:
                n = PARENTS[PARENTS[n]]
            return n

        def union(n1,n2):
            parentn1 = find(n1)
            parentn2 = find(n2)

            if parentn1 == parentn2:
                return [n1,n2]

            if RANK[parentn1]>=RANK[parentn2]:
                PARENTS[parentn2] = parentn1
                RANK[parentn1]+=1
            else:
                PARENTS[parentn1] = parentn2
                RANK[parentn2]+=1
            return None

        for x,y in edges:
            res = union(x,y)
            if res:
                return res

            