class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # identify fresh
                    fresh += 1
                elif grid[r][c] == 2: # add rotten to q
                    q.append((r, c))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            # even if len(q) updates, range() takes a snapshot
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    row, col = dr + r, dc + c
                    # if in bounds and fresh, make it rotten
                    if (row < 0 or col < 0 or
                        row == ROWS or col == COLS or
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
                
            time += 1
        
        return time if fresh == 0 else -1

