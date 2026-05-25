from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # all nodes are connected
        # no cycles
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visited = set()
        que = deque([(0, -1)])
        visited.add(0)
        while que:
            curr, parent = que.popleft()
            for neigh in adj[curr]:
                # why the fuck do I care about this
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                else:
                    que.append((neigh, curr))
                    visited.add(neigh)
        print(visited)
        return len(visited) == n