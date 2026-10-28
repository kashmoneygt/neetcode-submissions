class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squs = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                pos = 1 << (int(board[r][c]) - 1)
                if (
                    rows[r] & pos
                    or cols[c] & pos
                    or squs[(r // 3) * 3 + (c // 3)] & pos
                ):
                    return False
                
                rows[r] |= pos
                cols[c] |= pos
                squs[(r // 3) * 3 + (c // 3)] |= pos
        
        return True