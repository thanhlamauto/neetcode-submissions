class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for x in prices:
            if x < buy:
                buy = x
            else:
                profit = max(profit, x - buy)
        
        return profit