class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for stock in prices:
            minPrice = min(minPrice, stock)
            maxProfit = max(maxProfit, stock-minPrice)
        
        return maxProfit