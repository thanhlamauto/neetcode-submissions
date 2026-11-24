class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i], nums[i-1])
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i-1), dfs(i-2) + nums[i])
            return memo[i]
        n=len(nums)
        return dfs(n-1)
            