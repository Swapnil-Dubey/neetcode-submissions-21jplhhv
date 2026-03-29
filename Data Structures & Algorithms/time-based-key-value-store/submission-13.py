class TimeMap:

    def __init__(self):
        self.map = {}#key:[(value,timestmap)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((value,timestamp))
        else:
            self.map[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        currbest = None
        l = 0
        r = len(self.map[key])-1

        while l<=r:
            mid = (l+r)//2

            if self.map[key][mid][1]<=timestamp:
                currbest = self.map[key][mid][0]
                l = mid+1
            else:
                r = mid-1
        if currbest == None:
            return ""
        return currbest
        

        
