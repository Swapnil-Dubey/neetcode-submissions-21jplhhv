class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # can try sorting
        #but lets do the dict method first
        if len(s) != len(t):
            return False

        mys = {}
        myt = {}

        for a in range(len(s)):
            if s[a] in mys:
                mys[s[a]]+=1
            else:
                mys[s[a]] = 1
            
            if t[a] in myt:
                myt[t[a]]+=1
            else:
                myt[t[a]] = 1
        
        return mys == myt
            


        