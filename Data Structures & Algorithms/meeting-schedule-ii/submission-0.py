"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # return max number overlapping conference rooms at any time

        start = []
        end = []

        for i in intervals:
            start.append(int(i.start))
            end.append(int(i.end))
        
        start.sort()
        end.sort()


        stptr = 0
        endptr = 0

        res = 0
        absmax = res

        while stptr<len(start):
            if start[stptr]<end[endptr]:
                stptr+=1
                res+=1
                absmax = max(absmax,res)
            else:
                endptr+=1
                res-=1
        return absmax
            

        

