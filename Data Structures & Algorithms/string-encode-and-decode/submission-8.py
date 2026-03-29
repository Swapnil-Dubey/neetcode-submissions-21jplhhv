class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        #3#abc10#....
        l = 0
        while l<len(s)-1:
            num = ""

            while s[l]!="#":
                num+=s[l]
                l+=1
            
            num = int(num)
            word = ""

            l+=1
            while num>0:
                word+=s[l]
                l+=1
                num-=1
            
            
            res.append(word)
        return res

