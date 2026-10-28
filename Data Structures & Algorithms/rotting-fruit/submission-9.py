class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()
        
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        def addCell(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            
            grid[r][c] = 2
            q.append((r, c))
            
            nonlocal fresh
            fresh -= 1
        
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)
            
            time += 1
        
        return time if fresh == 0 else -1

                