class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []

        def dfs(i, total):
            if total == target:
                result.append(combination.copy())
                return
            
            if total > target or i == len(nums):
                return
            
            combination.append(nums[i])
            total += nums[i]
            dfs(i, total)

            num = combination.pop()
            total -= num

            dfs(i + 1, total)

        dfs(0,0)

        return result

            
                
            
            