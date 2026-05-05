class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0


        def expandPalindrome(i):
            nonlocal res

            l = i
            r = i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                l-=1
                r+=1
                res+=1
            
            l = i
            r = i+1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                l-=1
                r+=1
                res+=1


        for i in range(len(s)):
            expandPalindrome(i)
        
        return res