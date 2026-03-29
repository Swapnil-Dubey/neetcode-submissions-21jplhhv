class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #keep track of characters under window in a set to detecet duplicates in O(1) and move l+=1 until its out
        # set only has unique characters

        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1

        l = 0
        r = l+1

        longest = 1
        seen = set()
        seen.add(s[0])

        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest = max(longest, len(seen)) #imp lnogest keeps track of max value
            r+=1
        return longest

        