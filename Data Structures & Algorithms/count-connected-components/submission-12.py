class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [0]*n
        parent = [i for i in range(n)]







        # return parent of nth node in the graph
        def find(n):
            while n!=parent[n]:
                n = parent[parent[n]]
            return n


        def union(n1,n2):

            parentn1 = find(n1)
            parentn2 = find(n2)

            

            if rank[parentn1]>=rank[parentn2]:
                parent[parentn2]=parentn1
                if rank[parentn1]==rank[parentn2]:
                    rank[parentn2]+=1
            else:
                parent[parentn1]=parentn2

        for (n1,n2) in edges:
            union(n1,n2)
        

        seen = set()
        res = 0

        for i in range(n):
            seen.add(find(i)) #imp use set and use find function to find all unique parents

        return len(seen)

            