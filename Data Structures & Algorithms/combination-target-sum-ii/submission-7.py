class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        print(candidates)

        def dfs(i, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            if i == len(candidates) or candidates[i] > remaining:
                return
            path.append(candidates[i])
            dfs(i+1, remaining - candidates[i])
            path.pop()
            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j+=1
            dfs(j, remaining)
        
        dfs(0, target)
        return result


