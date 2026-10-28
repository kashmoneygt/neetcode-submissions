class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = [0] * 9, [0] * 9, [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c]) - 1
                mask = 1 << val

                if rows[r] & mask:
                    return False
                elif cols[c] & mask:
                    return False
                elif squares[(r // 3) * 3 + (c // 3)] & mask:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                squares[(r // 3) * 3 + (c // 3)] |= mask
        
        return True
