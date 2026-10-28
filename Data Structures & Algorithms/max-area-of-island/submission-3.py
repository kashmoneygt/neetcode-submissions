class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c) -> int: # to count an island
            if (r < 0 or c < 0 or
            r == ROWS or c == COLS or
            grid[r][c] == 0):
                return 0

            # setting to 0 removes need for visited set
            grid[r][c] = 0 # b/c we don't visit 0s
            
            return (1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = dfs(r, c)
                    res = max(res, size)
        
        return res

