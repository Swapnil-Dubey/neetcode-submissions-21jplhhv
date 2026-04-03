class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #output: min number of cpu cycles required to complete tasks

        #constraints: 1 <= tasks.length <= 1000
        #               0 <= n <= 100
        #edge cases: 
        #approach: count frequencies of each character, add that to a heapify max bcz we want to process high freq chars first
        #time Complexity
        #space complexity: 

        freqmap = {}

        for t in tasks:
            freqmap[t] = freqmap.get(t, 0)+1

        tasks = list(freqmap.values())

        heapq.heapify_max(tasks)

        q = deque()
        time = 0

        while tasks or q:
            time+=1
            if q and q[0][1]==time:
                popped = q.popleft()
                heapq.heappush_max(tasks, popped[0])
            if tasks: 
                first_task = heapq.heappop_max(tasks)
                first_task-=1
                if first_task:
                    q.append((first_task,time+n+1))
        return time

