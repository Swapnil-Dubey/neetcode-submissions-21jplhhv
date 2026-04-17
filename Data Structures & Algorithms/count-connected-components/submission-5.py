class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        PARENTS = [i for i in range(n)]
        RANK = [1]*n


        def parent(n):
            while PARENTS[n]!=n:
                n = PARENTS[PARENTS[n]]
            return n
        
        def union(n1,n2):

            if RANK[parent(n1)]>=RANK[parent(n2)]:
                PARENTS[parent(n2)] = parent(n1)
                RANK[parent(n1)]+=1
            else:
                PARENTS[parent(n1)] = parent(n2)
                RANK[parent(n2)]+=1
        
        for (x,y) in edges:
            union(x,y)

        parents = set()
        for i in range(n):
            parents.add(parent(i))
        return len(parents)
