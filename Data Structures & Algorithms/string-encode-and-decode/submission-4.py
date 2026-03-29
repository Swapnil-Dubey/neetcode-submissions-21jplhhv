class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
#s = 3#abc10#abcdefghij
#.        i j
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        l = ""
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            l = int(s[i:j])
            word = s[j+1:j+l+1]
            res.append(word)
            i = j+l+1
        return res
        
        

