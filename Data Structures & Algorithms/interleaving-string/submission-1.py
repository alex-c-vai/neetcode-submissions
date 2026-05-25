class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = [[-1] * (len(s2)+1) for _ in range(len(s1)+1)]
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if memo[i][j] != -1:
                return memo[i][j]
            
            k = i + j
            ans = False

            if i < len(s1) and s1[i] == s3[k]:
                ans = dfs(i+1, j)
            
            if not ans and j < len(s2) and s2[j] == s3[k]:
                ans = dfs(i, j+1)
            
            memo[i][j] = ans
            return memo[i][j]
        return dfs(0,0)