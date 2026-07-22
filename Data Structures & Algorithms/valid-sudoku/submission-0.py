class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = defaultdict(set)
        col_check = defaultdict(set)
        box_check = defaultdict(set)

        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] not in row_check[i]:
                    row_check[i].add(board[i][j])
                else:
                    return False

                if board[i][j] not in col_check[j]:
                    col_check[j].add(board[i][j])
                else:
                    return False
                
                box_idx = (i // 3) * 3 + (j // 3)
                if board[i][j] not in box_check[box_idx]:
                    box_check[box_idx].add(board[i][j])
                else:
                    return False
        return True