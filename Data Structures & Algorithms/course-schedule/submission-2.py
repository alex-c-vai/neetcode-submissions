from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        # build adjencency list; 1 -> 0 and indegree[0] = 1
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        
        que = deque()
        visitedNodes = 0

        for k in range(numCourses):
            if indegree[k] == 0:
                print(k)
                que.append(k)
        
        while que:
            node = que.popleft()
            visitedNodes += 1

            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    que.append(neigh)
        
        return visitedNodes == numCourses
