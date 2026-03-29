class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        #make window of sie s1
        resmapping = {}
        for s in s1:
            resmapping[s] = resmapping.get(s,0)+1

        l = 0
        r = 0
        for i in range(len(s1)-1):
            r+=1

        
        
        window = s2[l:r]
        mapping = {}
        for s in window:
            mapping[s] = mapping.get(s,0)+1
        

        while r<len(s2):
            mapping[s2[r]] = mapping.get(s2[r],0)+1
            if mapping == resmapping:
                return True
            else:
                mapping[s2[l]]-=1
                if mapping[s2[l]]==0:
                    mapping.pop(s2[l])
                l+=1
                r+=1
        return False
                
            
        