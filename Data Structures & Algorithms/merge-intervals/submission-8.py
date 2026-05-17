class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0]) #dont forget to sort

        res = []

        i = 0

        while i<len(intervals): #idea is that check the ith interval with recently added one, if it overlaps replace res[-1]
            if res:
                print(res)
                if res[-1][1]<intervals[i][0]:
                    res.append(intervals[i])
                else:
                    popped = res.pop()
                    res.append([min(popped[0],intervals[i][0]),max(popped[1],intervals[i][1])])
            else:
                res.append(intervals[i])
            i+=1
        
        return res


            