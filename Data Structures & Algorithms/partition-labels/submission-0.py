class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def check_status(dict1, dict2):
            for char in dict1:
                if dict1[char]!=dict2[char]:
                    return False
            return True

        # s = lowercase
        #return: [int] where each int is length of substrings
        #       split s into substrings of any size where each letter appears in max 1 substring


        #one way: make dict = {char:freq} 
        #       start curr substring. = "" and maintain a currdict = {} where each char in currdict freq must match the dict char frequency and its in order so 1 pass

        s_dict = {} #char:freq

        for c in s:
            if c in s_dict:
                s_dict[c]+=1
            else:
                s_dict[c]=1



        

        i = 0
        res = []

        while i<len(s):
            curr_dict = {s[i]:1} #char:freq seen so far             #{a:1}
            curr_string = s[i]                                      #"a"

            while check_status(curr_dict,s_dict) != True:
                i+=1
                if i>=len(s):
                    break
                curr_string+=s[i]
                if s[i] in curr_dict:
                    curr_dict[s[i]]+=1
                else:
                    curr_dict[s[i]]=1
            i+=1
            res.append(len(curr_string))
        return res



        
        

        