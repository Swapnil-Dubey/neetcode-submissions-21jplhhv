class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #window is valid if: sizeofwindow-mostfreqchar <=k

        #input = string s
        #output = length of longest valid window
        #constraints: 1<=s.length<=1000
            #0<=k<=s.length
        #pattern: sliding window
        #approach: l and r pointes (window), hashmap(dict) that keeps track of counts of each character 
            # in the window
        #time complexity: O(n)
        #space complexity: O(n)
        
        l =0
        r = 1
        window = {}
        window[s[l]] = window.get(s[l],0)+1
        mostfreqcharcount = 1
        mostfreqchar = s[l]
        res = 1

        while r<len(s):
            window[s[r]] = window.get(s[r],0)+1
            if mostfreqcharcount <window[s[r]]:
                mostfreqcharcount = window[s[r]]
                mostfreqchar = s[r]

            while (r-l+1)-mostfreqcharcount>k:
                window[s[l]]-=1
                l+=1
            
            res = max(res, r-l+1)
            
            r+=1
        return res
            
            

