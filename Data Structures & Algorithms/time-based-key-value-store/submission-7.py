class TimeMap:

    def __init__(self):
        #{key: [(timestamp, value)]}
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp,value))
        else:
            self.map[key] = [(timestamp,value)]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""

        l = 0
        r = len(self.map[key])-1
        currbest = ""

        while l<=r:
            mid = (l+r)//2

            if self.map[key][mid][0]<=timestamp:
                currbest = self.map[key][mid][-1]
                
                l = mid+1
            
            else:
                r = mid-1
        
        return currbest

        
