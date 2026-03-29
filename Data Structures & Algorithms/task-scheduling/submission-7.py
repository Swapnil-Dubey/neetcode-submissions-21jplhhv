class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Omlogn
        #since we only need to return number of cpu cycles lets convert to freq counts maxheap

        counts = {}
        for i in tasks:
            counts[i] = counts.get(i,0)+1

        tasks = []
        for i in counts:
            tasks.append(counts[i])

        heapq.heapify_max(tasks) #1,1
        queue = []#(3,1),(4,1)
        time = 0 #3
        while tasks or queue:
            time+=1 
            if queue and queue[0][0]==time:
                popped = queue.pop(0)[1]
                heapq.heappush_max(tasks, popped)

            if tasks:
                curr = heapq.heappop_max(tasks) 
                curr-=1
                if curr>0:
                    queue.append((time+n+1,curr))
        return time
                