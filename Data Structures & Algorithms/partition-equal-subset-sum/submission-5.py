class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        s = sum(nums) // 2

        dp = [False] * (s+1)
        dp[0] = True

        for num in nums:
            for i in range(s, num-1, -1):
                dp[i] = dp[i - num] or dp[i]
        return dp[s]



