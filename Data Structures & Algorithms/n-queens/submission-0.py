class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."]*n for _ in range(n)]
        cols, diag, anti = set(), set(), set()

        def dfs(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in anti:
                    continue
                
                board[row][col] = "Q"
                cols.add(col), diag.add(row-col), anti.add(row+col)

                dfs(row+1)

                board[row][col] = "."
                cols.remove(col), diag.remove(row-col), anti.remove(row+col)
        dfs(0)
        return result
