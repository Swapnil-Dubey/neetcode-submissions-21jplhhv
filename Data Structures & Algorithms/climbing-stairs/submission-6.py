class Solution:
    def climbStairs(self, n: int) -> int:
        # no. of ways to get to n = no. of ways to get to n-1 + no. of ways to get to n-2
        # base case = no. of ways to get to n == 1 = 1 and no. of ways to get to n == 2 = 2

        memo = {0:0, 1:1,2:2}

        #returns no. of ways to get to n
        def helper(n):
            if n in memo:
                return memo[n]

            memo[n] = helper(n-1)+helper(n-2)


            return memo[n]
        
        return helper(n)
