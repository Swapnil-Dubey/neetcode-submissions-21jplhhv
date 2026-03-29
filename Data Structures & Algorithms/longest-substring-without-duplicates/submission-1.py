class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

#constraints:0 <= s.length <= 1000
#edge cases: 0 length string
#pattern:sliding window
#approach: l -> r forms a window and keep a set of elements in this window, since subtring is a contiguous sequence within a string wihtout duplicates, as soon as r moves and encounters a duplicate, move l to remove the duplicate this way u get all possible non duplicate character continguous sequences in the string
#time complexity: O(n)

        l = 0
        r = l+1
        window = set()
        maxwindow = 0

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        window.add(s[l])
        maxwindow = len(window)

        while r<len(s):
            while s[r] in window: #is this a problem because what if l = r or l passes r?
                window.remove(s[l]) 
                l+=1
                # but wouldnt this be a problem does remove remove just the char at positoin l-1 or all occurences of that char OH WAIITTTT SETS CAN ONLY HAVE NON DUPLICATE CHARACTERS IN PYTHON!!!
            window.add(s[r])
            maxwindow =max(maxwindow, len(window))
            r+=1
        return maxwindow




