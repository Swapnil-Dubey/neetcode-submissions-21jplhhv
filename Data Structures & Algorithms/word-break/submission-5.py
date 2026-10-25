class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}



        def f(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                dp[i] = True
                return dp[i]

            for w in wordDict:
                if i+len(w)<=len(s):
                    if s[i:i+len(w)]==w:
                        if f(i+len(w)):
                            dp[i] = True
                            return dp[i]
                    else:
                        continue
                else:
                    dp[i] = False
            dp[i] = False
            return dp[i]

        return f(0)

        
            