class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def clear(r, c) -> None:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
                return
            
            grid[r][c] = "0"

            clear(r + 1, c)
            clear(r - 1, c)
            clear(r, c + 1)
            clear(r, c - 1)

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    # do a BFS where we clear the rest of the island starting with (r, c) in our queue
                    clear(r, c)
        
        return res

        
        