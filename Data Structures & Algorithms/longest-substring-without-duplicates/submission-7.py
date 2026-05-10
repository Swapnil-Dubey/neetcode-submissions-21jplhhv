class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        r = 0

        res = 0


        while r<=len(s)-1:
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res,r-l+1)



            r+=1
        return res


            

