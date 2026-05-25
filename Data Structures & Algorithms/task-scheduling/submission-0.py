import heapq
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for t in tasks:
            count[t] += 1
        heap = [(-count[t],t) for t in count]
        heapq.heapify(heap)
        que = deque([])
        time = 0

        while heap or que:
            time += 1
            if heap:
                _, task = heapq.heappop(heap)
                count[task] -= 1
                if count[task] > 0:
                    que.append((task, time+n))
            if que and que[0][1] == time:
                task, time = que.popleft()
                if count[task] > 0:
                    heapq.heappush(heap, (-count[task],task))
        return time

