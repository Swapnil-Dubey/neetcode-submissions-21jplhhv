class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 # number of jumps it takes to get to the target (last value of input arr)
        l = r = 0 # two pointers telling what window we're processing

        while r<len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,nums[i]+i)
            l = r+1
            r = farthest
            res+=1
            


        return res
