class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        board = grid
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == "0":
                return

            board[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "1":
                    res += 1
                    dfs(r, c)
        
        return res