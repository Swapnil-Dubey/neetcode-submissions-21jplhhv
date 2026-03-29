class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #valid window is when (windowsize - maxfreqcharinwindow <=k - if yes, then keep track of max window size)

        l = 0
        r = 0
        count = {}
        currmaxfreq = 0
        res =0 

        while r<len(s):
            count[s[r]] = count.get(s[r],0)+1
            currmaxfreq = max(currmaxfreq,count[s[r]])

            while (r-l+1)-currmaxfreq>k:
                count[s[l]]-=1 # why do we not need to  remove from count dict here if it hits 0 , also why dont we need to update currmaxfreq here what if the max freq goes down
                l+=1 
            
            res = max(res, r-l+1)
            r+=1
        return res