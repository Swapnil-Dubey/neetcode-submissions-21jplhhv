class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: string s
#output: length of longest substring without duplicate chars
#constraints: 0 <= s.length <= 1000 ,CONTIGUOS SUBSTRING
#edge cases: 0 length string, 1 length string
#pattern:sliding window
#approach: sliding window contiguous, keep removing elements from left until u dont have anymore duplicates
#           because the substring is contiguous so we have to remove chars until duplicate in the window is gone
#time complexity:O(n)
# O(n)

        seen = set()
        if len(s) == 0 or len(s) ==1:
            return len(s)
        l = 0
        r = l+1
        res = 0
        seen.add(s[l])
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res,len(seen))
            r+=1
        
        return res
            

