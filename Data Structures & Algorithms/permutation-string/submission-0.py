class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
#input:str s1, str s2
#output: True is s2 contains a permutation of s1, otherwise false
#constraints: both strings only lower case characters
#pattern: two hashmaps + sliding window
#time complexity:O(n=+m)
#space complexity: O(n*m)
        if len(s1)>len(s2):
            return False

        s1map = {}
        for c in s1:
            s1map[c] = s1map.get(c,0)+1
        
        l = 0
        r = 0
        for i in range(len(s1)-1):
            r+=1
        
        while r<len(s2):
            window = {}
            for c in s2[l:r+1]:
                window[c] = window.get(c,0)+1
            
            if window == s1map:
                return True
            l+=1
            r+=1
        return False

        
