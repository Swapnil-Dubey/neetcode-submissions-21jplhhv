class Solution:
    def longestPalindrome(self, s: str) -> str:
         #essentially, at every ith position (l = i, r = i) and try to expand in both directions as much as u can
        max = ""
        #odd case
        for i in range(len(s)):
            l = i
            r = i

            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if len(max)<r-l+1:
                    max = s[l:r+1]
               
                l-=1
                r+=1



        #even case


        for i in range(len(s)):
            if i == len(s)-1:
                continue
            l = i
            r = i+1

            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if len(max)<r-l+1:
                    max = s[l:r+1]
               
                l-=1
                r+=1
        return max
        