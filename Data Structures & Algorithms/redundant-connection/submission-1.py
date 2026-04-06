class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #start at no edges, check if adding an edge connected two already connected nodes

        parents = [i for i in range(len(edges)+1)]  # parents array needs to be 0 to n range indexed and also valued 
        rank = [1]*(len(edges)+1)
        res =[]

        def parent(n):
            while n!=parents[n]:
                parents[n] = parents[parents[n]] 
                n = parents[n]
            return n

        def union(n1,n2):
            parentn1 = parent(n1)
            parentn2 = parent(n2)

            if parentn1 == parentn2:
                return 0
            
            rankparentn1 = rank[parentn1]
            rankparentn2 = rank[parentn2]

            if rankparentn1>=rankparentn2:
                parents[parentn2] = parentn1
                rank[parentn1]+=1
            else:
                parents[parentn1] = parentn2
                rank[parentn2]+=1
            return 1
        
        for (a,b) in edges:
            ret = union(a,b)

            if ret == 0:
                res.append([a,b])
        return res[-1]
            
            
        