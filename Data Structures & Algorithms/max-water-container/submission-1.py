class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input = int [] heights
        #output: max amount of water a container can store
        

        # brute: max amount of water can be calculated by
        # - vol = min(height[i],height[i+k]) * k
        # use two pointers starting furthest out, keep max storable vol in check
        l = 0
        r = len(heights)-1
        maxvol = 0

        while l<r:
            vol = min(heights[l],heights[r]) * (r-l)
            if vol>maxvol:
                maxvol = vol
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return maxvol