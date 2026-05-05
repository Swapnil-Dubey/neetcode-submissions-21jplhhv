class Solution:
    def longestPalindrome(self, s: str) -> str:
        #longest substring that is a palindronme
        #subset of palindrome is a palindrome, so center palindrome at each position in the str
        # then try to expand as much as u can
        # even length palindrome edge case*
        maxlen = 0
        res = ""
        for i in range(len(s)):
            l =i
            r = i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if maxlen<r-l+1:
                    maxlen = r-l+1
                    res = s[l:r+1]

                l-=1
                r+=1
            l = i
            r = i+1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if maxlen<r-l+1:
                    maxlen = r-l+1
                    res = s[l:r+1]

                l-=1
                r+=1
        
        return res