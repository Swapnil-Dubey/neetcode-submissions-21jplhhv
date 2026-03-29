class Solution:
#.  4#neet4#code4#love3#you
    def encode(self, strs: List[str]) -> str:
        returnstr = ""
        for s in strs:
            lenstr = len(s)
            returnstr+= str(lenstr)+"#"+s
        return returnstr

    def decode(self, s: str) -> List[str]:
        returnlist = []
        i = 0
        while i <len(s):
            charnumber = ""
            returnstr = ""
            while s[i]!="#":
                charnumber+=s[i]
                i+=1
            print(charnumber)
            charnumber = int(charnumber)
            returnstr+=s[i+1:i+charnumber+1]
            i+=charnumber+1
            returnlist.append(returnstr)
        return returnlist




