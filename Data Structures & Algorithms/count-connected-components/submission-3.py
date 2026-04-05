class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        def getparent(n):
            while parent[n]!=n:
                n = parent[n]
            return n

        #returns 1 if succesful union, 0 if already connected
        def union(n1,n2):
            n1parent = getparent(n1)
            n2parent = getparent(n2)

            if n1parent == n2parent:
                return 0

            if rank[n1parent]>=rank[n2parent]:
                parent[n2parent] = n1parent
                rank[n2parent]+=1
            else:
                parent[n1parent] = n2parent
                rank[n1parent]+=1
            return 1

        res = n
        for (n1,n2) in edges:
            res-=union(n1,n2)
        return res