class TimeMap:

    def __init__(self):
        self.mapping = {} #key:[(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapping: 
            self.mapping[key].append((timestamp, value))
        else:
            self.mapping[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        if key in self.mapping:
            r = len(self.mapping[key])-1
        else:
            return ""
        currbest = None

        while l<=r:
            mid = (l+r)//2

            if self.mapping[key][mid][0]<=timestamp:
                currbest = self.mapping[key][mid][1]
                l = mid+1
            else:
                r = mid-1
        
    
        if not currbest:
            return ""
        else:
            return currbest
        
