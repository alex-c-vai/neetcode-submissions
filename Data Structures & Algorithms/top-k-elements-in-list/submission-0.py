from collections import deque, defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1
        
        heap = []
        heapq.heapify(heap)
        for num in counter:
            heapq.heappush(heap, (counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res