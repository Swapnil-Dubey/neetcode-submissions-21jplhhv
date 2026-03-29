class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input = [str]
        #output = list[list[str]]

        # constraints = strs[i] is lowercase english
        

        res = {}

        #key is gonna be the frequency list of each word

        for s in strs:
            freqlist = [0]*26
            for c in s:
                freqlist[ord(c)-ord('a')]+=1
                ####imppp:  a list cant be a dict key
            freqlist = tuple(freqlist)
            if freqlist in res:
                res[freqlist].append(s)
            else:
                res[freqlist] = [s]
        
        return list(res.values()) #its .values()
