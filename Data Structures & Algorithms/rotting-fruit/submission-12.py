class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = ((0, -1), (0, 1), (1, 0), (-1, 0))

        q = collections.deque()
        
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c)) # multi-source BFS
                elif grid[r][c] == 1:
                    fresh += 1      # track number of fresh
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)): # go through the current sources
                r, c = q.popleft()  # pop from left so we're not popping what we just added
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in-bounds and fresh, make rotten
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append((row, col)) 
                    fresh -= 1
            
            time += 1            
        
        # if we still have fresh oranges, we didn't get through all of them
        return time if fresh == 0 else -1