class Solution:
    def trap(self, height: List[int]) -> int:
        #input = int [] height
        #output = max water between bars
        #edge cases = zero storable water
        #pattern = arrays
        #approach = at psn i, storable water area = min(max(hl),max(hl))-height[i]
        #time complexity
        #space complexity

        l = 0
        r = len(height)-1

        maxleftheight = [0]*len(height)
        maxrightheight = [0]*len(height)
        currmax = 0
        for h in range(len(height)):
            currmax = max(currmax,height[h])
            maxleftheight[h] = currmax
        currmax = 0
        for h in range(len(height)-1,-1,-1):
            currmax = max(currmax,height[h])
            maxrightheight[h] = currmax
        

        res = 0

        for i in range(len(height)):
            if height[i]<min(maxleftheight[i],maxrightheight[i]):
                res+=min(maxleftheight[i],maxrightheight[i])-height[i]
        return res


