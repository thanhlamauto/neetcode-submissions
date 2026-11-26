class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = float("-inf")
        rest = 0
        sold = 0

        for price in prices:
            prev_hold, prev_sold = hold, sold
            hold = max(hold, rest-price)
            rest = max(rest, prev_sold)
            sold = prev_hold + price
        
        return max(sold, rest)