class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            freq = tuple(freq)
            if freq in seen:
                seen[freq].append(s)
            else:
                seen[freq]=[s]
        return list(seen.values())