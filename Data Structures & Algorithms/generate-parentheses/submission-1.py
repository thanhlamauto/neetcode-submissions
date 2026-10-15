class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = ""

        def dfs(path, i, j):
            nonlocal n

            if len(path) == 2*n:
                result.append(path)
                return 
            
            if i < n:
                dfs(path + "(", i+1, j+1)

            if j > 0:
                dfs(path + ")", i, j-1)
            
        dfs(path, 0, 0)
        return result
            
