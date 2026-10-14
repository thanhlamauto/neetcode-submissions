class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []
        path = []

        def dfs(i, total):
            if total == target:
                result.append(path.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            path.append(candidates[i])
            total += candidates[i]

            dfs(i+1, total)

            path.pop()
            total -= candidates[i]
            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, total)
        
        dfs(0, 0)
        return result