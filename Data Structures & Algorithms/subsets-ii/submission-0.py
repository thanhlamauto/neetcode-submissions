class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        path = []

        def dfs(i):
            if i == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i+1)
            
            path.pop()
            j = i+1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j)
        
        dfs(0)
        return result












































            