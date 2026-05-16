class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start dfs at pacific ocean neighbouring cells, atlantic neighboring cells, mark reachable from each then find the intersection
        ROWS = len(heights)
        COLS = len(heights[0])

        reachablebypacific = set()
        reachablebyatlantic = set()
        final =[]

        def dfs(r,c, res):
            res.add((r,c))

            if (r+1)>=0 and (r+1)<=ROWS-1 and heights[r+1][c]>=heights[r][c] and (r+1,c) not in res:
                dfs(r+1,c,res)
            if (r-1)>=0 and (r-1)<=ROWS-1 and heights[r-1][c]>=heights[r][c] and (r-1,c) not in res:
                dfs(r-1,c,res)
            if (c+1)>=0 and (c+1)<=COLS-1 and heights[r][c+1]>=heights[r][c] and (r,c+1) not in res:
                dfs(r,c+1,res)
            if (c-1)>=0 and (c-1)<=COLS-1 and heights[r][c-1]>=heights[r][c] and (r,c-1) not in res:
                dfs(r,c-1,res)


            




        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r,c,reachablebypacific) # adds all spots reachable by r,c to reachablebypacific
                
                if r == ROWS-1 or c == COLS-1:
                    dfs(r,c,reachablebyatlantic) # adds all spots reachable by r,c to reachablebyatlantic
        


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in reachablebypacific and (r,c) in reachablebyatlantic:
                    final.append([r,c])
        return final
                




        







