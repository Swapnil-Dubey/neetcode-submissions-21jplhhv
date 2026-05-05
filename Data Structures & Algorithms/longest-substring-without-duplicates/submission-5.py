class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input = string s
        # output = int l : length of longest substring(CONTIGUOUS) without duplicates
        # constraints: 0<=len(s)<=1000
        #edge cases: len(s) == 0
        #            s only contains 1 letter (all duplicates)
        #approach and pattern: two pointers, keep a hashset of chars in this window,
        #   and keep expanding r, as soon as u encounter a duplicate, keep moving l up until
        #   there are no more duplicates. 
        #   keep track of global max(res)
        #time complexity:
        #space complexity:


        l = 0
        r = 0
        res = 0
        seen = set()
        


        if len(s) == 0:
            return 0

        seen.add(s[0])
        
        while r<len(s):
            res = max(res, len(seen))
            r+=1
            while r<len(s) and l<=r and s[r] in seen:
                seen.remove(s[l])
                l+=1
            if r<len(s):
                seen.add(s[r])
        return res



