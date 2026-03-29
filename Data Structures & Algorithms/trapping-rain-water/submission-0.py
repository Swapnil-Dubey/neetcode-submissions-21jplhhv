class Solution:
    def trap(self, height: List[int]) -> int:
        currmax = 0
        maxlh = [0]*len(height)
        for i in range(len(height)):
            maxlh[i]=currmax
            currmax = max(currmax, height[i])
        print(maxlh)
        currmax = 0
        maxrh = [0]*len(height)

        for i in range(len(height)-1,-1,-1):
            maxrh[i] = currmax
            currmax = max(currmax, height[i])
        print(maxrh)
        totalarea = 0
        for i in range(len(height)):
            if min(maxlh[i],maxrh[i])-height[i]>0:
                totalarea+=min(maxlh[i],maxrh[i])-height[i]

        
        return totalarea


