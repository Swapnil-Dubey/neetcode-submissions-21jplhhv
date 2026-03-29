class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        lettert = {}

        for c in s:
            if c in letters:
                letters[c]+=1
            else:
                letters[c]=1
        for c in t:
            if c in lettert:
                lettert[c]+=1
            else:
                lettert[c]=1
        

        return letters==lettert
        