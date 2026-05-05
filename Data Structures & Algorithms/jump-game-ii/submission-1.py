class Solution:
    def jump(self, nums: List[int]) -> int:
        #find the min steps to reach last position, given we can always reach

        #bfs type soln

        res = 0 #number of jumps it takes to reach a dest
        l = r = 0 #tell us the current window

        while r<len(nums)-1:

            farthest = 0
            for i in range(l,r+1):
                farthest = max(nums[i]+i,farthest)
            l = r+1
            r = farthest


            res+=1
        return res
    

