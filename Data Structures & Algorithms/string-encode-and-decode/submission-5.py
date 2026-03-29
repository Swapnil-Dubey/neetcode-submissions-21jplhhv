class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i!=len(s): # len s = 14
            num = ""
            currword = ""
            while s[i]!="#":
                num+=s[i]
                i+=1
            i+=1
            num = int(num)
            while num>0:
                currword+=s[i]
                num-=1
                i+=1
            res.append(currword)
        return res



