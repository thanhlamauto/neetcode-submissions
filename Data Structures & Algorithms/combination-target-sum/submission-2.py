class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        nums.sort()

        def dfs(i, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if i == len(nums) or nums[i] > remaining:
                return
            path.append(nums[i])
            dfs(i, remaining - nums[i])
            path.pop()
            dfs(i+1, remaining)

        dfs(0, target)
        return result