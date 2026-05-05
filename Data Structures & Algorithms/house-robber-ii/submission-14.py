class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        memo = {0:nums[0],1:max(nums[0],nums[1])}
        memo2 = {1:nums[1],2:max(nums[1],nums[2])}
        #returns max money stolen upto and including house n
        def money(n, memo):
            if n in memo:
                return memo[n]
            
            memo[n] = max(money(n-2, memo)+nums[n],money(n-1, memo))
            return memo[n]
        return max(money(len(nums)-1, memo2), money(len(nums)-2, memo))