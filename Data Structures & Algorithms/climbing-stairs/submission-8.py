class Solution:
    def climbStairs(self, n: int) -> int:
        # number of distinct ways to reach nth staircase = number of ways to reach n-1th staircase + number of ways to reach n-2th staircase

        d = {0:1,1:1,2:2}

        def dfs(n):
            if n in d:
                return d[n]
            else:
                d[n] = dfs(n-1)+dfs(n-2)
                return d[n]
        return dfs(n)
        