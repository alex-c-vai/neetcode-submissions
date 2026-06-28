class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            for word in wordDict:
                j = len(word)
                if i+j <= len(s) and s[i:i+j] == word:
                    if dfs(i+j): # if the next index can be split into valid words
                        memo[i] = True
                        return memo[i]
            
            memo[i] = False
            return memo[i]
        
        return dfs(0)