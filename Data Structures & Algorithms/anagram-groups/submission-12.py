class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}#(freqlist):[list of words]
        for str in strs:
            freqlist = [0]*26
            for c in str:
                freqlist[ord(c)-ord('a')]+=1
            freqlist = tuple(freqlist)
            if freqlist in res:
                res[freqlist].append(str)
            else:
                res[freqlist] = [str]
        return list(res.values())