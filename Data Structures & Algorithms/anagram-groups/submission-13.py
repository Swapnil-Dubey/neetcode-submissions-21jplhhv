class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maptolistofwords = {}

        for s in strs:
            freqmap = [0]*26
            for c in s:
                freqmap[ord(c)-ord('a')]+=1
            freqmap = tuple(freqmap)
            if freqmap in maptolistofwords:
                maptolistofwords[freqmap].append(s)
            else:
                maptolistofwords[freqmap] = [s]
        return list(maptolistofwords.values())
            