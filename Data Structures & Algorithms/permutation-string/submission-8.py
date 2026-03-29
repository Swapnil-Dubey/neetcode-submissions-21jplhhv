class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create a window of size s1 and traverse through s2 looking for counts = {} of s1
        if len(s1)>len(s2):
            return False

        s1counts = {}
        for c in s1:
            s1counts[c] = s1counts.get(c,0)+1
        
        l = 0
        r = 0
        for i in range(len(s1)):
            r+=1
        
        currcounts = {}

        for c in s2[l:r]:
            currcounts[c] = currcounts.get(c,0)+1
        
        while r<len(s2):
            if currcounts == s1counts:
                return True
            currcounts[s2[r]] = currcounts.get(s2[r],0)+1
            r+=1
            currcounts[s2[l]]-=1
            if currcounts[s2[l]]<=0:
                currcounts.pop(s2[l])
            l+=1
        return currcounts == s1counts

        
        