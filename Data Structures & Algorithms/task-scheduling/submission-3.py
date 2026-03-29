class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #input = str [] tasks -> tasks[i] = A-Z, int n
        #output = number of minimum cpu cycles reqd to complete all tasks
        #constraints:  1 <= tasks.length <= 1000, 0<=n<=100
        #edge cases: len(tasks) == 1, n==0, n == 100, len(tasks) == 1000
        #pattern: heap, and queue
        #approach: min heapify the tasks array freq of chars O(n), after an element is popped, reduce it by 1 and put it into the queue with time to be taken out of the queue and back into the heap 
        #time complexity:  O(n)+O(n)+o(mlogn) 
        #space complexity:O(m)



        
        charfreq = {}

        for i in tasks:
            charfreq[i] = charfreq.get(i, 0) + 1

        tasks = []

        for i in charfreq:
            tasks.append(charfreq[i])
        
        heapq.heapify_max(tasks)
        queue = []

        time = 0
        while queue or tasks:
            time+=1 

            if queue: 
                if queue[0][1]==time:
                    tobeaddedtotasks = queue.pop(0)
                    heapq.heappush_max(tasks, tobeaddedtotasks[0])

            if tasks:
                curr = heapq.heappop_max(tasks)
                curr-=1
                if curr>0:
                    queue.append((curr, time+n+1))
        return time








