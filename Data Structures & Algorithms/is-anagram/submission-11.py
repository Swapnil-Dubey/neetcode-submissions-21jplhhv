class Solution:
    def isAnagram(self, s: str, t: str)->bool:
        # edge case: both empty strings
        # normal case: not anagrams,    
            #   anagrams
        # to be anagram:  same length


        if len(s)!=len(t):
            return False
        
        #anagram: count of each char in word is equal to the count of each char in other word

        #26 chars in alphabet
        #make a matrix of 26 0s and trigger to 1 acc to the ord() of the char
        matrix1 = [0]*26
        matrix2 = [0]*26
        for i in range(len(s)):
            matrix1[ord(s[i])-ord('a')]+=1
            matrix2[ord(t[i])-ord('a')]+=1
        return matrix1==matrix2