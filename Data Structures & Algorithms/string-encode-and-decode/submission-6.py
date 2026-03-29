class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        #.   5#Hello

        res = []
        i = 0
        while i < len(s)-1:
            j = i
            length = ""
            while s[j]!="#":
                length+=s[j]
                j+=1
            print(length)
            length = int(length)
            j+=1


            word = ""
            while length>0:
                word+=s[j]
                j+=1
                length-=1
            
            res.append(word)
            print(word)
            i=j
        return res

            

