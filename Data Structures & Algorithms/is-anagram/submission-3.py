class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.getDict(s)==self.getDict(t)

    def getDict(self, string: str) -> dict:
        d = {}
        for s in string:
            if s in d.keys():
                d[s]+=1
            else:
                d[s]=1
        return d

