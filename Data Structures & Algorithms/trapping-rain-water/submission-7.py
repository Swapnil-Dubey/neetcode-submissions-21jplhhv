class Solution:
    def trap(self, height: List[int]) -> int:
#constraints 1 <= height.length <= 1000
        #    0 <= height[i] <= 1000
#edge cases: height at i is bigger than min(max(height[l]),max(height[r])) at i, height len = 1
#pattern:arrays
#approach: storablewater[i] = min(max(height[l]),max(height[r]))-height[i]
#time complexity: O(n)
#space complexity: O(n)


        leftmaxheights = [0]*len(height)
        rightmaxheights = [0]*len(height)

        currmax = 0
        for i in range(len(height)):
            leftmaxheights[i]=currmax
            currmax = max(currmax, height[i])


        currmax = 0
        for i in range(len(height)-1,-1,-1):
            rightmaxheights[i]=currmax
            currmax = max(currmax, height[i])
        
        res = [0]*len(height)
        for i in range(len(height)):
            res[i] = max(min(leftmaxheights[i],rightmaxheights[i])-height[i],0)
        return sum(res)


        
