class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)

        def dfs(rems):
            if not rems:
                result.append(path.copy())
                return

            for rem in rems:
                path.append(rem)
                new_rems = rems.copy()
                new_rems.remove(rem)
                dfs(new_rems)
                path.pop()
        dfs(nums)

        return result

            
            