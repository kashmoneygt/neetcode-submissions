class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: fresh += 1
                if grid[r][c] == 2: q.append((r, c))

        ROWS, COLS = len(grid), len(grid[0])
        def process(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))
            nonlocal fresh
            fresh -= 1

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                process(r + 1, c)
                process(r - 1, c)
                process(r, c + 1)
                process(r, c - 1)

            time += 1

        return time if fresh == 0 else -1