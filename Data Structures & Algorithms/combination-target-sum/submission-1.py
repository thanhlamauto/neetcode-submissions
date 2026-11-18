class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(i):
            if i == len(nums):
                return
            if sum(path) > target:
                return
            elif sum(path) == target:
                result.append(path.copy())
                return
            path.append(nums[i])
            dfs(i)
            path.pop()
            dfs(i+1)

        dfs(0)
        return result