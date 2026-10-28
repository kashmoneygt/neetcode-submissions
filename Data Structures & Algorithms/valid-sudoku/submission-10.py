class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                position = 1 << (int(board[r][c]))
                if position & rows[r]: return False
                if position & cols[c]: return False
                if position & squares[(r // 3) * 3 + (c // 3)]: return False

                rows[r] |= position
                cols[c] |= position
                squares[(r // 3) * 3 + (c // 3)] |= position
            
        return True

