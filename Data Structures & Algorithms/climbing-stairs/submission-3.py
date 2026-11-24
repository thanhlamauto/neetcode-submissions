from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def dfs(n):
            if n == 0 or n == 1:
                return 1
            return dfs(n-1) + dfs(n-2)
        return dfs(n)
