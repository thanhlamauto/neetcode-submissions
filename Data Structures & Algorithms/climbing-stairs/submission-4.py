from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n == 0 or n == 1:
                return 1
            if n in memo:
                return memo[n]
            else:
                memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]
        return dfs(n)
