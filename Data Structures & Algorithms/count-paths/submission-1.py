class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        res = 0
        dirs = [(0,1), (1,0)]
        
        # at each index we have two choices: move down or move right
        def dfs(r, c):
            if r == m-1 or c == n-1:
                return 1
            if memo[r][c] != -1:
                return memo[r][c]
            # cache all iterations
            memo[r][c] = sum([dfs(r+dr, c+dc) for dr, dc in dirs])
            return memo[r][c]
        
        return dfs(0,0)