class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        currmax = 0
        for i in range(len(height)):
            leftmax[i] = currmax
            currmax = max(currmax, height[i])

        currmax = 0
        for i in range(len(height)-1,-1,-1):
            rightmax[i]=currmax
            currmax = max(currmax,height[i])

        res = [0]*len(height)
        for i in range(len(height)):
            if height[i]>min(leftmax[i],rightmax[i]):
                continue
            else:
                res[i] = min(leftmax[i],rightmax[i])-height[i] #remember height can be > min(leftmax[i],rightmax[i])

        return sum(res)
        
