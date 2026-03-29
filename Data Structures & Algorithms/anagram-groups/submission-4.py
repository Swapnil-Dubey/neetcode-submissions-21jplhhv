class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # data structure: dict with keys as ordered str, value as 
            # list of anagrams
        # time complexity: O(m*n) : m is number of strings 
            # and n is length of longest str
        # edge cases: empty list, single element, no anagrams, empty string

        d = dict() #{}
        for string in strs: 
            sortedstr = ''.join(sorted(string)) 
            if sortedstr in d: 
                d[sortedstr].append(string) 
            else:
                d[sortedstr] = [string] 
        return list(d.values())
            


    

    # sorting a string
    # convert dict.values python return type to list output
    #d[sortedstr] = d[sortedstr].append(string) 
    #   append() modifies the list in place and returns None.
