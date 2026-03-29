class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        # 3#abc10#abc.....

        res = []

        c = 0
        while c<len(s):
            num = ""
            while s[c]!="#":
                num+=s[c]
                c+=1
            
            c+=1
            num=int(num)

            word = ""

            while num>0:
                word+=s[c]
                c+=1
                num-=1
            res.append(word)


        return res



            





