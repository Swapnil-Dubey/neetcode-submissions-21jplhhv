class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {0:0, 1:0}
        def mincost(i):
            #mincost to get to 0th or 1th position = 0 we start there
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(cost[i-1]+mincost(i-1),cost[i-2]+mincost(i-2))
            return memo[i]
            
        
        return mincost(len(cost))
