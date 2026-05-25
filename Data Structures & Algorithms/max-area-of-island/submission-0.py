class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r,c):
            if (r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==0):
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in dirs:
                area += dfs(r+dr, c+dc)
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(dfs(row, col), res)
        
        return res
                