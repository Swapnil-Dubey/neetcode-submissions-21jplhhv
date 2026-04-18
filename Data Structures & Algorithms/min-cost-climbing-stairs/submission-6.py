class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost to reach floor n = min((cost to reach i-1 + cost at i-1),
                                    #(cost to reach i-2 + cost at i-2))

        #base case: cost to reach floor 1 = cost at 0, cost to reach floor 2 = min(cost at i = 0,cost at i=1)
                    #cost to reach floor 0 = 0

        memo = {0:0,1:0, 2: min(cost[0],cost[1])}

        def helper(n):
            if n in memo:
                return memo[n]
            

            memo[n] = min(helper(n-1)+cost[n-1],helper(n-2)+cost[n-2])

            return memo[n]
        return helper(len(cost))