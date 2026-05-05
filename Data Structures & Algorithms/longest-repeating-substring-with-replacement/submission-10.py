class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #as long as windowsize-freqofmaxfreqchar <=k, we are good otherwise l+=1


        l = 0
        r = 0
        res = 1
        freq = {}
        maxfreqchar = s[r]
        

        if len(s) == 1:
            return 1


        while r<=len(s)-1:
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]] = 1
            if freq[s[r]]>freq[maxfreqchar]:
                maxfreqchar = s[r]
            

            while (r-l+1)-freq[maxfreqchar]>k:
                freq[s[l]]-=1
                maxfreqcharfreq = 0
                maxfreqchar = ''
                for char in freq:
                    if freq[char]>maxfreqcharfreq:
                        maxfreqcharfreq = freq[char]
                        maxfreqchar = char

                l+=1
            res = max(res,r-l+1)
            r+=1
        return res

