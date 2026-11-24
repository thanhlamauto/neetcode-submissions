class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i == 0 or i == 1:
                return cost[i]
            if i in memo:
                return memo[i]
            memo[i] = min(dfs(i-1), dfs(i-2)) + cost[i]
            return memo[i]
        n = len(cost)
        return min(dfs(n-1), dfs(n-2))
            
            