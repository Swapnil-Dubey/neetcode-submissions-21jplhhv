class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        di={}
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c]=1
        for c in t:
            if c in di:
                di[c]+=1
            else:
                di[c]=1
        return d==di
        
        