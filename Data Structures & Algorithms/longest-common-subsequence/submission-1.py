class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[-1] * len(text2) for _ in range(len(text1))]

        def dfs(r,c):
            if r == len(text1) or c == len(text2):
                return 0
            print(r,c,len(text1), r==len(text1))
            if cache[r][c] != -1:
                return cache[r][c]
            
            if text1[r] == text2[c]:
                cache[r][c] = 1 + dfs(r+1, c+1)
            else:
                cache[r][c] = max(dfs(r, c+1), dfs(r+1,c))
            
            return cache[r][c]

        return dfs(0,0)