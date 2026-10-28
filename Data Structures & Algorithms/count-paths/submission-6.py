class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        
        level = [1] * COLS
        for _ in range(ROWS - 1):
            newLevel = [1] * COLS
            for i in range(COLS - 2, -1, -1):
                newLevel[i] = newLevel[i + 1] + level[i]
            level = newLevel

        return level[0]