class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                position = 1 << int(board[r][c])
                if rows[r] & position: return False
                if cols[c] & position: return False
                if squares[(r // 3) * 3 + (c // 3)] & position: return False

                rows[r] |= position
                cols[c] |= position
                squares[(r // 3) * 3 + (c // 3)] |= position
            
        return True

