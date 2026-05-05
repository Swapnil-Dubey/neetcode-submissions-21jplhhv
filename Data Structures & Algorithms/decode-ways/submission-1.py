class Solution:
    def numDecodings(self, s: str) -> int:
        #if a substring starts with 0, doesnt map to anything
        #at each pointer either decode 1 character out or decode 2 character outs then 1+decoding rest of the string

        #either take 1 digit or 2 digits
        cache = {}
        #answers: how many ways can i decode the substirng s[i:]
        def dfs(i):
            if i>=len(s):
                return 1
            if s[i]=='0':
                return 0
            if i in cache:
                return cache[i]
            res = dfs(i+1)

            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
                res+=dfs(i+2)
            cache[i] = res
            return res
        return dfs(0)