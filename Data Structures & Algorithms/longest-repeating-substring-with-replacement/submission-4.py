class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # valid window = len(window)-freqmaxfreqchar(window) >=k

        seen = {}

        if len(s) == 1:
            return 1
        
        l = 0
        r = 1
        maxres = 0
        seen[s[l]] = seen.get(s[l],0)+1
        maxfreqcharfreq = 1

        
        while r<len(s):
            seen[s[r]] = seen.get(s[r],0)+1
            
            if maxfreqcharfreq<seen[s[r]]:
                maxfreqcharfreq = seen[s[r]]

            if (r-l+1)-maxfreqcharfreq<=k:
                maxres = max(maxres, r-l+1)
                
            else:
                seen[s[l]]-=1
                l+=1
            r+=1
            
                
            
        return maxres
            


