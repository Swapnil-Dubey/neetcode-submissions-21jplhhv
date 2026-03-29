class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
#input:str s1, str s2
#output: True is s2 contains a permutation of s1, otherwise false
#constraints: both strings only lower case characters
#pattern: two hashmaps + sliding window
#time complexity:O(n+m)
#space complexity: O(26)
        if len(s1)>len(s2):
            return False

        s1map = {}
        for c in s1:
            s1map[c] = s1map.get(c,0)+1
        
        l = 0
        r = 0
        window = {}

        for i in range(len(s1)):
    
            window[s2[r]] = window.get(s2[r],0)+1
            r+=1

        
        while r<len(s2):
            if window == s1map:
                return True

            window[s2[r]] = window.get(s2[r],0)+1
            r+=1

            

            window[s2[l]]-=1
            if window[s2[l]]<=0:
                window.pop(s2[l])
            l+=1


            
            

        return window == s1map

        
