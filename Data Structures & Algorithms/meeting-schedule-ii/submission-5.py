"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0 # max value of len currmeetings so far
        currmeetings = []
        heapq.heapify(currmeetings)


        intervals.sort(key = lambda x:x.start)


        for i in range(len(intervals)):
            if currmeetings:
                while currmeetings and currmeetings[0][0]<=intervals[i].start:
                    heapq.heappop(currmeetings)
            heapq.heappush(currmeetings,(intervals[i].end,intervals[i].start))

            res = max(res,len(currmeetings))
        return res
        