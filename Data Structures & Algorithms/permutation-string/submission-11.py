class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        l = 0
        r = 0

        if len(s1) == 1:
            return s1 in s2
        
        for i in range(len(s1)-1):
            r+=1
        
        targetfreqmap = {}
        currfreqmap = {}

        for i in s1:
            targetfreqmap[i] = targetfreqmap.get(i, 0)+1
        
        for i in s2[l:r+1]:
            currfreqmap[i] = currfreqmap.get(i,0)+1
        
        while r<len(s2):
            if currfreqmap == targetfreqmap:
                return True
            
            currfreqmap[s2[l]]-=1
            if currfreqmap[s2[l]]<=0:
                currfreqmap.pop(s2[l])
            l+=1
            r+=1
            if r<len(s2):
                currfreqmap[s2[r]] = currfreqmap.get(s2[r],0)+1
        return False

