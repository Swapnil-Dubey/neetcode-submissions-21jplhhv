class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Not a FIFO so use a heap
        # heap = [(time, count of char)]

        freq = {}

        for i in tasks:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        

        tasks = list(freq.values())
        heapq.heapify_max(tasks)
        q = deque()
        #tasks is a maxheap
        #make a q alongside it that stores task,timetogetout
        time = 0
        while tasks or q:
            time+=1
            if q and q[0][1]==time:
                heapq.heappush_max(tasks,q.popleft()[0])
            if tasks:
                curr = heapq.heappop_max(tasks)
                curr-=1
                if curr==0:
                    continue
                else:
                    q.append((curr,time+n+1))

        return time




