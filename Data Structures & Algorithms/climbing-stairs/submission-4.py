class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1 for _ in range(n)]
        def dfs(i):
            if i >= n: # n is our targe
                return i == n # returns 1 or 0
            if cache[i] != -1:
                return cache[i]
            # this is the recursive part where we climb one or two steps
            res =  dfs(i+1) + dfs(i+2)
            cache[i] = res
            return res
    
        return dfs(0) # we start from step 0