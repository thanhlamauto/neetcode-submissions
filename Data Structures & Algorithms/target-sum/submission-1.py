class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for num in nums:
            new_dp = defaultdict(int)
            for s, count in dp.items():
                new_dp[s + num] += count
                new_dp[s - num] += count
            dp = new_dp
        
        return dp.get(target, 0)

                
