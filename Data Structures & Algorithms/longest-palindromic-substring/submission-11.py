class Solution:
    def longestPalindrome(self, s: str) -> str:
        #idea is that at every ith position, have 2 pointers at i =l and i = r or r = i+1(even case)
        reslen = 0
        res = ""
        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                reslen = max(reslen,r-l+1)
                if reslen==r-l+1:
                    res = s[l:r+1]
                l-=1
                r+=1
            
        #even length palindrome
            l = i
            r = i+1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                reslen = max(reslen,r-l+1)
                if reslen==r-l+1:
                    res = s[l:r+1]
                l-=1
                r+=1





        return res