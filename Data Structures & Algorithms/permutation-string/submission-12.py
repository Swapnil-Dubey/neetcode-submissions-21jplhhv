class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #howw to do this whole q!! 
        #we're just looking for s1 (or its permutations) in s2 (window is of size s1)


        if len(s1)>len(s2):
            return False


        lookingfor = {}

        for s in s1:
            if s in lookingfor:
                lookingfor[s]+=1
            else:
                lookingfor[s] = 1
        


        l = 0
        r = len(s1)-1

        currentseen = {}

        for i in range(0,r+1):
            if s2[i] in currentseen:
                currentseen[s2[i]]+=1
            else:
                currentseen[s2[i]] = 1

        

        while r<len(s2):
            if currentseen == lookingfor:
                return True

            currentseen[s2[l]]-=1
            if currentseen[s2[l]] == 0: #impp do these checks first, before moving the pointer
                currentseen.pop(s2[l])
            l+=1
            


            r+=1
            if r<len(s2):
                if s2[r] in currentseen:
                    currentseen[s2[r]]+=1
                else:
                    currentseen[s2[r]] = 1
            else:
                break
        return False
            



