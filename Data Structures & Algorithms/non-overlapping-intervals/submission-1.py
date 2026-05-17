class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = []
        resremovals = 0

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue

            if res[-1][1]>intervals[i][0]:
                if res[-1][1]<intervals[i][1]:
                    continue
                else:
                    res.pop()
                    res.append(intervals[i])
            else:
                res.append(intervals[i])
        return len(intervals)-len(res)
        
