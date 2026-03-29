class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d1 = {}
            d2 = {}
            for i in range(len(s)):
                if s[i] in d1:
                    d1[s[i]]+=1
                else:
                    d1[s[i]] = 1
            
            for x in range(len(t)):
                if t[x] in d2:
                    d2[t[x]]+=1
                else:
                    d2[t[x]] = 1
            if d1 == d2:
                return True
            else:
                return False
                
        else:
            return False