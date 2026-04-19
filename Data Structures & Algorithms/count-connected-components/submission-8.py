class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        PARENTS = [i for i in range(n)]
        RANK = [1]*n


        def find(n):
            while n!=PARENTS[n]:
                n = PARENTS[PARENTS[n]]
            return n

        def union(n1,n2):
            parentn1 = find(n1)
            parentn2 = find(n2)

            if RANK[parentn1]>=RANK[parentn2]:
                PARENTS[parentn2] = parentn1
                RANK[parentn1]+=1
            else:
                PARENTS[parentn1] = parentn2
                RANK[parentn2]+=1
        
        for x,y in edges:
            union(x,y)

        res = set()
        for i in range(n):
            res.add(find(i))
        
        return len(res)

    
        

