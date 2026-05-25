from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ingree = [0] * numCourses
        adj = defaultdict(list)
        res = []

        for pre in prerequisites:
            ingree[pre[0]] += 1
            adj[pre[1]].append(pre[0])
        print(ingree)
        print(adj)
        que = deque([])

        for node in range(numCourses):
            if ingree[node] == 0:
                que.append(node)
        nodesVisited = 0
        while que:
            node = que.popleft()
            nodesVisited += 1
            res.append(node)
            for neigh in adj[node]:
                ingree[neigh] -= 1
                if ingree[neigh] == 0:
                    que.append(neigh)
        
        return res if nodesVisited == numCourses else []