class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window as long as the windowsize-maxfreqcharfreq<=k, we can keep increasing window size. If condition is not valid then move l+=1
        l = 0
        r = 0
        freq = {s[0]:1}
        mostfreqcharinwindow = s[0]
        res = 0



        while r<=len(s)-1:
            while (r-l+1) - freq[mostfreqcharinwindow]>k:
                freq[s[l]]-=1
                maxfreq = 0
                for char in freq:
                    if freq[char]>maxfreq:
                        mostfreqcharinwindow = char
                        maxfreq = freq[char]
    

                l+=1
            res = max(res,r-l+1)
            r+=1
            if r<len(s) and s[r] in freq:
                freq[s[r]]+=1
            else:
                if r<len(s):
                    freq[s[r]]=1
            if r<len(s) and freq[s[r]]>freq[mostfreqcharinwindow]:
                mostfreqcharinwindow = s[r]
        return res
