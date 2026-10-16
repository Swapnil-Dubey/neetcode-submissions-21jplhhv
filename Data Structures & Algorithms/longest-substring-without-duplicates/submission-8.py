class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 1
        if len(s) == 0:
            return 0
        seen = set()

        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            else:
                res = max(res, r-l+1)
            seen.add(s[r])
            r+=1
        return res
