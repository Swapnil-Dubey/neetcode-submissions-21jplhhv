class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            sorteds = ''.join(sorted(s))
            storethis = seen.get(sorteds,[])
            storethis.append(s)
            seen[sorteds] = storethis
        return list(seen.values())