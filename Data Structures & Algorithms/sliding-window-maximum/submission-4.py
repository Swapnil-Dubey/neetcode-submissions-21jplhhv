class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #sliding window of size k
        # monotonically decreasing deque, leftmost value in the sliding window is the maximum in that range

        q = deque()

        l=0
        r=0

        res = []

        for i in range(k):
            while q and nums[r]>q[-1]:
                q.pop()
            
            q.append(nums[r])


            r+=1
        r-=1

        res.append(q[0])
        



        while r!=len(nums)-1:
            if nums[l]==q[0]:
                q.popleft()
            l+=1
            r+=1
            while q and nums[r]>q[-1]:
                q.pop()
            
            q.append(nums[r])
            res.append(q[0])
        return res




