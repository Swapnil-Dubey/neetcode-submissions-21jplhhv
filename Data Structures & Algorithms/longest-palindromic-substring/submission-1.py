class Solution:
    def longestPalindrome(self, s: str) -> str:
        # center at each positin in the str, and expand from there (even length palindrome edge case) 

        res = ""
        reslen = 0


        for i in range(len(s)):
            #oddlength

            l,r = i,i

            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                if r-l+1>reslen: # whats the issue here?
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            

            #even length
            l,r = i,i+1 # why does this work????

            while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                if r-l+1>reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
