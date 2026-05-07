class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        s = s.lower()

        while l<r:
            while l<r and not s[l].isalnum():  #imppp when u are moving pointers always check for the outer condition (l<r)if that doesnt meet then we're done anyway
                l+=1
            while r>l and not s[r].isalnum():
                r-=1
            if l<r and s[l]!=s[r]:
                return False
            
            l+=1
            r-=1
        return True

