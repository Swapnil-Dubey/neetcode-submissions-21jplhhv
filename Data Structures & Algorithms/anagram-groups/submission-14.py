class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #length is same
        # count of each char is same

        #edge case: empty string
        seen = {}
        for s in strs:
            curr = [0]*26
            for c in s:
                curr[ord(c)-ord('a')]+=1
            curr = tuple(curr)
            if curr in seen:
                seen[curr].append(s)
            else:
                seen[tuple(curr)] = [s]
        return list(seen.values())