class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # just get frequencies of each char in  the tasks list
        freq = {}
        for c in tasks:
            freq[c] = freq.get(c,0)+1
        
        tasks = []
        for i in freq:
            tasks.append(freq[i])

        heapq.heapify_max(tasks)

        queue = []

        time = 0
        while tasks or queue:
            if queue:
                stillwaiting = []
                for i in queue:
                    if i[0]<=time:
                        heapq.heappush_max(tasks, i[1])
                    else:
                        stillwaiting.append(i)
                queue = stillwaiting
            if not tasks:
                time+=1
                continue
            curr = heapq.heappop_max(tasks)
            curr-=1

            if curr>0:
                queue.append((time+n+1,curr))
            time+=1
        return time
        