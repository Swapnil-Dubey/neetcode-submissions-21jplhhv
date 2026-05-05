class Solution:
    def longestPalindrome(self, s: str) -> str:
        # trick is that a substring of a palindrome centered in the center is also a palindrome

        #   so we set mid to each char and start expanding

        res = ''
        reslen = 0

        def expandPalindrome(i):
            nonlocal res
            nonlocal reslen
            l = i
            r = i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                currlen = r+1-l
                if currlen>=reslen:
                    reslen = currlen
                    res = s[l:r+1]
                l-=1
                r+=1
            
            l = i
            r = i+1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                currlen = r+1-l
                if currlen>=reslen:
                    reslen = currlen
                    res = s[l:r+1]
                l-=1
                r+=1


        for i in range(len(s)):
            expandPalindrome(i)
        
        

        
        
        return res
                