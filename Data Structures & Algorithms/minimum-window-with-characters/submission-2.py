class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #have and need counts for overall condition
        # hashmap for freq char counting

        #if have == need (all required chars according to the needed hashmap
        #   should be directly equal to each other)
        needmap = {}
        havemap = {}
        have = 0
        need = 0
        reslen = 1001
        res = ""

        for c in t:
            if c in needmap:
                needmap[c]+=1
            else:
                needmap[c] = 1

        need = len(needmap)
        
        l = 0
        r = 0

        while r<=len(s)-1:
            if s[r] in needmap:
                if s[r] in havemap:
                    havemap[s[r]]+=1
                else:
                    havemap[s[r]]=1
                if havemap[s[r]]==needmap[s[r]]:
                    have+=1
                


                
                    while have==need:
                        if have == need:
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

       

            