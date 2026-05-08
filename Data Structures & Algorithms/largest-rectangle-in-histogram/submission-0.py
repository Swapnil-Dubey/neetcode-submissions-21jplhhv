class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #keep track of max area currently

        maxArea = 0
        stack = [] #pair: index,height

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h: #then pop this -1th height, and check max creatable rectangle from that height and extend h backward
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start, h))
        

        #entries left in stack now = heights that were able to be extended to the end of the histogram

        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))

        return maxArea
