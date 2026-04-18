class Solution:
    def countSubstrings(self, s: str) -> int:
        #input = string s
        #output = no. of subsctrings within s that are palindromes
        #constraints: 1 <= s.length <= 1000
        #             s consists of lowercase English letters.
        #pattern: two(3) pointers
        #approach: start at each position i as the center of a palindrome and expand from there(even length palindrome edge case)
        #edge cases:len(s) == 1
        # time complexity:O(n^2)
        # space complexity:O(1)

        res = []

        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                res.append(s[l:r+1])
                l-=1
                r+=1
            
            l,r = i,i+1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                res.append(s[l:r+1])
                l-=1
                r+=1
        return len(res)