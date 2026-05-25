"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        que = deque([node])
        copies = {}
        copies[node] = Node(node.val)
        while que:
            curr = que.popleft()
            for neigh in curr.neighbors:
                if neigh not in copies:
                    copies[neigh] = Node(neigh.val)
                    que.append(neigh)
                copies[curr].neighbors.append(copies[neigh])
        
        return copies[node]



        
            