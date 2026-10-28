class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        res = 0

        def dfs(r, c) -> int:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )
        
        for r in range(ROWS):
            for c in range(COLS):
                size = dfs(r, c)
                res = max(res, size)
        
        return res