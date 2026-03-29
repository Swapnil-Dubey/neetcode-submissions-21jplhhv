class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input:string s
        #output: int res
        #constraints: 0 <= s.length <= 1000
        #edge cases: s of length 0, 1
        #pattern: sliding window
        #approach: since we have to return lenght of longest substring without duplicates
        #   take 2 pointers, l and r, and a set() of what characters are in l->r if r hits a char already in the set, means it has
        #   already hit a duplicate so move l +=1 and remove from set until duplicate is gone from the left side. Do all this while keeping
        #   track of the largest len of the set
        #time complexity: O(n)
        #space complexity:O(n)
        
        l = 0
        r= l+1
        seen = set()
        res = 0

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            seen.add(s[l])
            while r<len(s):
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[r])
                res = max(res, len(seen))
                r+=1
        return res

        #JUST DONT FORGET TO INCREMENT R *******

