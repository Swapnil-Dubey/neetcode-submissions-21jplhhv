class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedword = {}

        for s in strs:
            if "".join(sorted(s)) in sortedword:
                sortedword["".join(sorted(s))].append(s) # imp adding to value (list) of dict
            else:
                sortedword["".join(sorted(s))] = [s]
        return sortedword.values()