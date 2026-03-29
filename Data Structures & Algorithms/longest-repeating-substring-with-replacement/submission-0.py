class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #size of window - maxfreq in window should be <= k for the window to be valid 
        #we want the longest valid window in our string

        count = {}
        maxf = 0

        l = 0
        r = 0

        res = 0

        while r<len(s):
            count[s[r]] = 1+count.get(s[r],0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1)-maxf > k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res




