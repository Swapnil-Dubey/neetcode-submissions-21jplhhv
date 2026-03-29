class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        l = 0
        r = 0

        window = {}
        window[s2[l]]=1

        for i in range(len(s1)-1):
            r+=1
            window[s2[r]] = window.get(s2[r],0)+1

        targetwindow = {}
        for c in s1:
            targetwindow[c] = targetwindow.get(c,0)+1
        
        while r<len(s2):
            if window == targetwindow:
                return True
            
            r+=1
            if r==len(s2):
                break
            window[s2[r]] = window.get(s2[r],0)+1

            window[s2[l]]-=1
            if window[s2[l]]<=0:
                del window[s2[l]]
            l+=1
        return False



        
