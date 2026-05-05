class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input = list of intervals
        #output = list of non overlapping intervals that cover all intervals in the input
        #brute force/approach: start iterating from the end, keep taking 2 intervals at a time, merge them if there is a overap otherwise move on to the next 2

        #edge cases = intervals len == 1
        #           start == end
        

        intervals.sort() #onlogn
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if i == 0:
                continue
            prev = res[-1]
            curr = intervals[i]

            if curr[0]<=prev[1]:
                res[-1] = [min(prev[0],curr[0]),max(curr[1],prev[1])]
            else:
                res.append(curr)
        return res


