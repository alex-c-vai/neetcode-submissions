class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        moves = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r,c,i):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in visited:
                return False
            if word[i] == board[r][c] and i == len(word)-1:
                return True
            visited.add((r,c))
            res = any([dfs(r+dr, c+dc, i+1) for dr, dc in moves])
            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False