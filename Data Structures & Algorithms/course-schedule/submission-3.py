from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        ingree = [0] * numCourses
        res = []

        for dest, src in prerequisites:
            ingree[dest] += 1
            adj[src].append(dest)

        que = deque([])

        for course in range(numCourses):
            if ingree[course] == 0:
                que.append(course)
        
        visitedNodes = 0

        while que:
            node = que.popleft()
            visitedNodes += 1
            
            for neigh in adj[node]:
                ingree[neigh] -= 1
                if ingree[neigh] == 0:
                    que.append(neigh)
        
        return visitedNodes == numCourses





