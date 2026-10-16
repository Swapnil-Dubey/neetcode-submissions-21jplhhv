class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])

        res = []
        

        for i in intervals:
            removed= []

            while res and res[-1][1]>=i[0]:
                removed = res.pop()
            if removed:
                res.append([min(i[0],removed[0]),max(i[1],removed[1])])
            else:
                res.append(i)

        return res