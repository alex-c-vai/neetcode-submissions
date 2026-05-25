from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        components = 0

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        for node in range(n):
            if node not in visited:
                components += 1
                que = deque([node])
                while que:
                    curr = que.popleft()
                    for neigh in adj[curr]:
                        if neigh not in visited:
                            visited.add(neigh)
                            que.append(neigh)
        return components

        