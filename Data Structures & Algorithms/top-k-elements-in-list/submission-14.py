class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        #input = int [] nums, int k 
        #output = int [] res (k most freq elements in nums)
        #constraints: 1<=len(nums)<=10^4
                    # -1000<=nums[i]<=1000
                    # 1<=k<=number of distinct elements in nums
        #edge cases: len(nums) == 1, all distinct elements, k == number of elements, k == 1
        # time complexity:
        #space complexity:
        # pattern and approach: create hashset of element frequences, create a max heap that stores (freq,el) and heappop that k times


        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        
        heap = []
        for i in freq:
            heapq.heappush_max(heap,(freq[i],i))
        res = []
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])

        return res