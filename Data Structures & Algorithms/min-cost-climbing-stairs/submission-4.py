class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        #returns the cost to get to ith step
        memo = {0:0,1:0}
        def costs(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = min(costs(n-1)+cost[n-1],costs(n-2)+cost[n-2])
                return memo[n]

        return costs(len(cost))