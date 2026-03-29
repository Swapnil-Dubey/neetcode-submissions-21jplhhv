class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            seens = {}
            seent = {}
            for c in s:
                if c in seens:
                    seens[c]+=1
                else:
                    seens[c]=1

            for c in t:
                if c in seent:
                    seent[c]+=1
                else:
                    seent[c]=1
            return seens==seent
        return False
            
        