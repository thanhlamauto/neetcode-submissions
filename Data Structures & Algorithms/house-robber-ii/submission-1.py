class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]

        memo = {}
        def dfs(i, k):
            if i < k:
                return 0
            if i == k:
                return nums[k]
            if (i, k) in memo:
                return memo[(i, k)]
            memo[(i, k)] = max(dfs(i-1, k), dfs(i-2, k) + nums[i])
            return memo[(i, k)]
            
        return max(dfs(n-1, 1), dfs(n-2, 0))