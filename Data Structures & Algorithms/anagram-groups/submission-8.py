class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}
        for s in strs:
            currmapp = [0]*26
            for c in s:
                currmapp[ord(c)-ord('a')] += 1
            currmapp = tuple(currmapp)
            if currmapp in mapp:
                mapp[currmapp].append(s)
            else:
                mapp[currmapp] = [s]
        return list(mapp.values())