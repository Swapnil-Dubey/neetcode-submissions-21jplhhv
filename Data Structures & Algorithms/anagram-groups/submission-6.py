class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            if tuple(freq) in res:
                res[tuple(freq)].append(s)
            else:
                res[tuple(freq)] = [s]
        return list(res.values())
