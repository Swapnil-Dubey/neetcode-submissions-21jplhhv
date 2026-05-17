class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #sorting always comes in handy for interval problems

        #case 1: newinteval doesnt overlap with 1st interval or last interval then just add it in the correct position (start or end) and return
        # 2 intervals are overlapping if newinterval doesnt come before or after the other interval
    

        res = []
        for i in range(len(intervals)):
            #edge case before current interval

            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]: # in this case we just add the current ith interval
                res.append(intervals[i])
            else:
                #there is an overlap with current interval
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]




        res.append(newInterval)
        return res
