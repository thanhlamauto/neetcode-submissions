class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []

        def dfs(rems):
            if not rems:
                result.append(permutation.copy())
                return
            
            for rem in rems:
                permutation.append(rem)
                new_rems = rems.copy()
                new_rems.remove(rem)
                dfs(new_rems)
                permutation.pop()
        dfs(nums)

        return result
            