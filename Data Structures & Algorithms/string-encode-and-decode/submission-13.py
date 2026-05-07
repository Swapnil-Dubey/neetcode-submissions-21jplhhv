class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res+=str(len(s))+"#"+s 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            currnum = ""
            currword = ""
            while s[i]!="#": 
                currnum+=s[i]
                i+=1
            #i is at # now
            currnum = int(currnum)
            for _ in range(currnum):
                i+=1
                currword+=s[i]
            res.append(currword)

            #i is at last letter now
            i+=1
        return res


            
            
