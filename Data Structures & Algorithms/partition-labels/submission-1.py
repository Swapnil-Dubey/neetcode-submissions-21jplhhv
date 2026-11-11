class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #last_psn_dict

        last_psn_dict = {}

        for i in range(len(s)):
            last_psn_dict[s[i]] = i

        res = []
        curr_string = ""
        curr_dict = {} #char:last position so far

        i = 0
        end = 0
        size = 1


        while i<len(s):
            end = max(last_psn_dict[s[i]], end)
            if i == end:
                res.append(size)
                size = 0
            size+=1
            
        
        
            i+=1
            
        return res

            

        