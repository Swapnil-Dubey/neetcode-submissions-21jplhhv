class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        memo = {0:0, 1:0 }
        def f(n):
            if n in memo:
                return memo[n]
            
            memo[n] = min(f(n-1)+cost[n-1],f(n-2)+cost[n-2])
            return memo[n]
        return f(len(cost))
