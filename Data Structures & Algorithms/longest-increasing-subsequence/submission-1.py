class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(n-2, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                elif nums[j] == nums[i]:
                    dp[i] = max(dp[i],dp[j])
        print(dp)
        return max(dp)