class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose the matrix (switch elements across diagonals)
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        # reverse each row
        for row in matrix:
            row.reverse()