class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, seen, prevVal):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seen or heights[r][c] < prevVal:
                return

            seen.add((r, c))
            dfs(r - 1, c, seen, heights[r][c])
            dfs(r + 1, c, seen, heights[r][c])
            dfs(r, c - 1, seen, heights[r][c])
            dfs(r, c + 1, seen, heights[r][c])
        
        atl, pac = set(), set()
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c] - 1)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c] - 1)
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0] - 1)
            dfs(r, COLS - 1, atl, heights[r][COLS - 1] - 1)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    res.append((r, c))

        return res
