class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        currmax = 0
        while l<r:
            # area of water = min(height1, height2)*(indexh2-indexh1)
            h1 = heights[l]
            h2 = heights[r]

            currarea = min(h1,h2)*(r-l)

            currmax = max(currarea,currmax)

            # since min height is the one thats bounding area
            # we can take a chance of getting a higher height even while
            # reducing width by moving the pointer with the lower height to the next one

            if h1>h2:
                r-=1
            else:
                l+=1
        return currmax
        