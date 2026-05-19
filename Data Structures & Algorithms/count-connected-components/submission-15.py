class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        PARENTS = [i for i in range(n)]
        rank = [1]*n



        #finds parent of n using path compression
        def find(n):
            while n!=PARENTS[n]:
                n = PARENTS[PARENTS[n]]
            return n

        #unions n1, n2, increase rank only if rank of both is the same. 
        def union(n1,n2):
            parentn1 = find(n1)
            parentn2 = find(n2)
            if rank[parentn1]>rank[parentn2]:
                PARENTS[parentn2] = parentn1

            elif rank[parentn2]>rank[parentn1]:
                PARENTS[parentn1] = parentn2
            else:
                PARENTS[parentn2] = parentn1
                rank[parentn1]+=1
            


                
        


        for (a,b) in edges:
            union(a,b)
        
         # rn it doesnt necessarily contain the topmost parent for each node

        for i in range(len(PARENTS)):
            PARENTS[i] = find(PARENTS[i])

        return len(set(PARENTS))
