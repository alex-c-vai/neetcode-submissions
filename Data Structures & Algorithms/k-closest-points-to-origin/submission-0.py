import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        res = []

        for px, py in points:
            euc = px**2 + py**2 # we don't need to worry about sqrt
            heapq.heappush(heap, (euc, (px,py)))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res