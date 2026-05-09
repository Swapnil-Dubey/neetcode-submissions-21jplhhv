class TimeMap:

    def __init__(self):
        #for this one store {key:<value,time>}

        self.timemap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value,timestamp))
        else:
            self.timemap[key] = [(value, timestamp)]

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        else:
            #binary search for timestamp closest <= timestamp
            l = 0
            r = len(self.timemap[key])-1
            res = None
            while l<=r:
                mid = (l+r)//2
                if self.timemap[key][mid][1]<=timestamp:
                    res = self.timemap[key][mid][0]
                    l = mid+1
                else:
                    r = mid-1
            if res == None:
                return ""
            else:
                return res




        
