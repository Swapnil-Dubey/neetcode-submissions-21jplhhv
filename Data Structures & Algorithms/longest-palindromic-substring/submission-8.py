class Solution:
    def longestPalindrome(self, s: str) -> str:
        #input: string s
        #output: longest substring of s that is a palindrome
        #constraints: s is digits or eng letters
        #   1<=len(s)<=1000
        #edge cases: len(s) == 1
        #               handle even length palindrome and odd length palindromes differently

        # approach and pattern: start from the center of the palindrome and expand outward at all positions of the string s
        reslen = 1
        res = s[0]
        for i in range(len(s)):
            #odd length case
            l = i
            r = i



            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if r-l+1>reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
                



            #even length case
            l = i
            r = i+1



            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if r-l+1>reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res

