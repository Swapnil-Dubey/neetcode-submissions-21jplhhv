class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {0:nums[0],1:max(nums[0],nums[1])}
        def maxcash(i):
            if i in memo:
                return memo[i]
            memo[i] = max(maxcash(i-1),maxcash(i-2)+nums[i])
            return memo[i]

        return maxcash(len(nums)-1)