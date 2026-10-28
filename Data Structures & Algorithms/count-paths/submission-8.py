class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        level = [1] * n

        for _ in range(m - 1):
            newLevel = [1] * n
            for c in range(n - 2, -1, -1):
                newLevel[c] = newLevel[c + 1] + level[c]
            level = newLevel
        
        return level[0]