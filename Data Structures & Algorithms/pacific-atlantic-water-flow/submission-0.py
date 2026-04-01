class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # input: heights[r][c] list height above sea level at r,c
        #output = 
        # constraints: water can flow to neighbor cell with height equal or lower
        #  approaach : start at the edge node and dfs  on the edge nodes to mark all the nods reachable from that edge node
                #       do these separately for pacific and atlantic 
        ROWS = len(heights)
        COLS = len(heights[0])
        pacificvisited = set()
        atlanticvisited = set()
        respacific = []
        resatlantic = []
            

        
        


        def dfspacific(r,c,reslist,prevheight):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in pacificvisited or heights[r][c]<prevheight:
                return
            
            reslist.append((r,c))
            pacificvisited.add((r,c))
            

            dfspacific(r+1,c,reslist,heights[r][c])
            dfspacific(r-1,c,reslist,heights[r][c])
            dfspacific(r,c-1,reslist,heights[r][c])
            dfspacific(r,c+1,reslist,heights[r][c])

            return reslist

        def dfsatlantic(r,c,reslist,prevheight):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in atlanticvisited or heights[r][c]<prevheight:
                return
            
            reslist.append((r,c))
            atlanticvisited.add((r,c))

            dfsatlantic(r+1,c,reslist,heights[r][c])
            dfsatlantic(r-1,c,reslist,heights[r][c])
            dfsatlantic(r,c-1,reslist,heights[r][c])
            dfsatlantic(r,c+1,reslist,heights[r][c])

            return reslist
        

        for r in range(ROWS):
            for c in range(COLS):
                if r==0 or c==0:
                    res = dfspacific(r,c,[],heights[r][c])
                    if res:
                        respacific.extend(res)
                if r==ROWS-1 or c==COLS-1:
                    res = dfsatlantic(r,c,[],heights[r][c])
                    if res:
                        resatlantic.extend(res)
        
        return list(set(respacific).intersection(resatlantic))
                    


        
            

            



