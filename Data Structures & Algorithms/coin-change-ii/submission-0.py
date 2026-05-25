class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        memo = dict()

        def dfs(i, total):
            if total == amount:
                print(1)
                return 1
            if i >= len(coins) or total >= amount:
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            # for each coin there are 2 options
            # take it or skip and move on to the next
            print(total)
            memo[(i,total)] =  dfs(i, total+coins[i]) + dfs(i+1, total)
            return memo[(i,total)]
        
        return dfs(0, 0)