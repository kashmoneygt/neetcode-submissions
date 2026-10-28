class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))
        
        def addCell(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in visit:
                return
            
            visit.add((r, c))
            q.append((r, c))
            

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            dist += 1