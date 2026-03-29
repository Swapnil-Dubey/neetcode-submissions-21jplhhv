class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            currfreq = [0]*26
            for c in s:
                currfreq[ord(c)-ord('a')]+=1
            currfreq = tuple(currfreq)
            if currfreq in res:
                res[currfreq].append(s)
            else:
                res[currfreq] = [s]
        return list(res.values())
