class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {0:0,1:0}

        #min cost to reach ith staircase = min (min cost to reach i-1th + cost at i-1, min cost to reach i-2th + cost at i-2)

        def dfs(n):
            if n in d:
                return d[n]
            
            d[n] = min(dfs(n-1)+cost[n-1],dfs(n-2)+cost[n-2])
            return d[n]
        return dfs(len(cost))
