class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #valid winodw if len(window)-maxfreqcharfreq <=k

        freq = {}
        maxfreqcharfreq = 1
        
        res = 0

        l = 0
        r = 1
        maxfreqchar =s[l]

        freq[s[l]] = 1

        if len(s) == 1:
            return 1
        
        while r<len(s):
            freq[s[r]] = freq.get(s[r],0)+1
            if freq[s[r]]>maxfreqcharfreq:
                maxfreqcharfreq = freq[s[r]]
                maxfreqchar = s[r]

            if (r-l+1)-maxfreqcharfreq<=k:
                res = max(r-l+1, res)
            else:
                if s[l] == maxfreqchar:
                    maxfreqcharfreq-=1
                freq[s[l]]-=1
                l+=1
            r+=1
        return res
