class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {} #word's char freq counts:[list of words that match this]


        for word in strs:
            freq = [0]*26
            for c in word:
                freq[ord(c)-ord('a')]+=1
            freq = tuple(freq)
            if freq in seen:
                seen[freq].append(word)
            else:
                seen[freq] = [word]
        return list(seen.values())
