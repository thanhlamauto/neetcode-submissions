class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        found = False

        def dfs(i, j, k):
            if k == len(word) - 1:
                return True

            tmp = board[i][j]
            board[i][j] = "#"

            for dx, dy in moves:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == word[k+1]:
                    if dfs(x, y, k+1):
                        board[i][j] = tmp
                        return True
            
            board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False