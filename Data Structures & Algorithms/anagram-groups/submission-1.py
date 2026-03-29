class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #{sortedstring:list of anagrams}
        returndict = {}
        for s in strs:
            if tuple(sorted(s)) in returndict:
                returndict[tuple(sorted(s))].append(s)
            else:
                returndict[tuple(sorted(s))] = [s]
        returnlist = []
        for l in returndict.values():
            returnlist.append(l)
        return returnlist




        