class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map: # O1
            self.map[key].append((value,timestamp)) #O1
        else:
            self.map[key] = [(value,timestamp)]#O1

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        else:
            #search for (value,timestamp) with timestamp right less than or eq to timestamp argument
            l = 0
            r = len(self.map[key])-1 #remember we binary search on index in a list, not its values
            currbest = 0
            currbestindex = None
            while l<=r:
                mid = (l+r)//2
                if self.map[key][mid][-1]<=timestamp:
                    # if currbest <=self.map[key][mid][-1]: # dont really need currbest here, we just check if the curr timestamp is less
                    # #than or eq to timestamp then keep track of index, otherwise binary search on rest
                    #     currbest = max(self.map[key][mid][-1],currbest)
                    currbestindex = mid
                    l = mid+1
                else:
                    r=mid-1
        if currbestindex==None: # need to handle this separately
            return ""
        
        return self.map[key][currbestindex][0]
            
                

# {key:[list of (value,timestamp)]}


#output: time based key value structure
#constraints:1 <= key.length, value.length <= 100
#   key and value only include lowercase English letters and digits.
#   1 <= timestamp <= 1000

#pattern: binary search on key then on timestamp
#time complexity: 
#space complexity:



        
