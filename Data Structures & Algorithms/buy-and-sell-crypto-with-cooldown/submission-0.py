class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        memo = [-1] * len(prices)

        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if memo[i] != -1:
                return memo[i]
            cd = dfs(i+1, buy)
            if buy:
                # if we are buying, the profit will the the future price minus today's price
                buy = dfs(i+1, not buy) - prices[i]
                return max(buy, cd)
            else:
                # if we are holding, then we cannot buy again next day
                sell = dfs(i+2, not buy) + prices[i]
                return max(sell, cd)

        return dfs(0, True)
