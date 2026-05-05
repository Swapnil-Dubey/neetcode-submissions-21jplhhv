class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return(nums[0])
        memo = {0:nums[0],1:max(nums[0],nums[1])}
        #returns max money stolen upto and including house n
        def money(n):
            if n in memo:
                return memo[n]
            
            memo[n] = max(money(n-2)+nums[n],money(n-1))
            return memo[n]
        return money(len(nums)-1)