from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # store indegree list
        indegree = [0] * numCourses
        # adjecency matrix for BFS traversal with a queue
        adj = [[] for _ in range(numCourses)]
        res = []

        # build up our adj and indegree
        for destination, source in prerequisites:
            indegree[destination] += 1
            adj[source].append(destination)
        
        que = deque()
        nodesVisited = 0

        # BFS will always start with nodes that don't have any dependencies
        for course in range(numCourses):
            if indegree[course] == 0:
                que.append(course)
        
        while que:
            node = que.popleft()
            nodesVisited += 1
            res.append(node)

            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    que.append(neighbour)
        
        return res if numCourses == nodesVisited else []
        
