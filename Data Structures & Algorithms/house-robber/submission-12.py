class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {0:nums[0], 1:max(nums[0],nums[1])}


        #return max amountof money u can steal up to and including ith position
        def money(i):
            if i in memo:
                return memo[i]
            memo[i] = max(money(i-1),money(i-2)+nums[i])
            return memo[i]
        return money(len(nums)-1)

