class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #shortest substring of s that contains all chars of t

        needmap = {}

        for c in t:
            if c in needmap:
                needmap[c]+=1
            else:
                needmap[c] = 1
        
        need = len(needmap)
        have = 0
        havemap = {}

        res = ""
        reslen = 1001


        l = 0
        r = 0

        while r<=len(s)-1:
            if s[r] in needmap:
                if s[r] in havemap:
                    havemap[s[r]]+=1
                else:
                    havemap[s[r]] = 1
            
                if havemap[s[r]]==needmap[s[r]]: #imp, cant do >= here bcz that would increment have variable multiple times for the same character (only increment have if we are exactly ==)
                    have+=1
            

            while have == need:
                if r-l+1<reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                
                if s[l] in havemap:
                    havemap[s[l]]-=1
                    if havemap[s[l]]<needmap[s[l]]:
                        have-=1
                l+=1
            r+=1
        

        return res


        


       