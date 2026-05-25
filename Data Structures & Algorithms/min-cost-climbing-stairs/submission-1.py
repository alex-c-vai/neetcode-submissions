class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost) + 1)
        def dfs(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            one = dfs(i+1)
            two = dfs(i+2)
            cache[i] = cost[i] + min(one, two)
            return cache[i]
        
        return min(dfs(0), dfs(1))