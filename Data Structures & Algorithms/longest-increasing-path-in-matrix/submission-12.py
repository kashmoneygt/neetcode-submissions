class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = {}

        def dfs(r, c, prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            
            dp[(r, c)] = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c])
            )
            return dp[(r, c)]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, matrix[r][c] - 1)

        return max(dp.values())
