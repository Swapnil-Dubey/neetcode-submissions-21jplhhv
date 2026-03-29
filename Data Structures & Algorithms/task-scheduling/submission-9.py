class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqmap = {}

        for i in tasks:
            freqmap[i] =freqmap.get(i, 0)+1

        tasks = []

        for i in freqmap:
            tasks.append(freqmap[i])
        # [3,2,1]

        heapq.heapify_max(tasks)

        queue = []
        time = 0

        while queue or tasks:
            time+=1
            if queue and queue[0][1]==time:
                curr = queue.pop(0)
                heapq.heappush_max(tasks, curr[0])
            if tasks:
                curr = heapq.heappop_max(tasks)
                curr-=1
                if curr>0:
                    queue.append((curr,time+n+1))
        return time

