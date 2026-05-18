class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        count = 0
        while r<len(nums)-1:
            count+=1
            best = 0
            for j in range(l,r+1):
                best = max(best,j+nums[j])
            l = r+1
            r = best
        return count

        




