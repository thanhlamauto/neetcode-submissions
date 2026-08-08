class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        upper = max(piles)
        lower = math.ceil(sum(piles) / h)

        def eat_all(piles, mid, h):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/mid)
            return hour


        l, r = lower, upper
        res = upper
        while l <= r:
            mid = l + ((r-l) // 2)
            if eat_all(piles, mid, h) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
