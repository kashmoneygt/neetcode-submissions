class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # mark col
                    if r > 0:
                        matrix[r][0] = 0 # mark row
                    else:
                        rowZero = True


        # Zero out matrix (except marker row/col)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Set first column to 0s
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # Set first row to 0s
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
