class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input = int[] heights
        #output = 2 bars to form container, max amount of water a container can store

        l =0
        r = len(heights)-1
        best = 0

        #bounded by the minimum height bar
        while l<r:
            best = max(best,min(heights[l],heights[r])*(r-l))

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return best

