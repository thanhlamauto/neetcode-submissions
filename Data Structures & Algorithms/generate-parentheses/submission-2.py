class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def dfs(i, j):
            if i == n and j == 0:
                result.append("".join(path))
                return 
            
            if i < n:
                path.append("(")
                dfs(i+1, j+1)
                path.pop()
            
            if j > 0:
                path.append(")")
                dfs(i, j - 1)
                path.pop()
        
        dfs(0, 0)
        return result
