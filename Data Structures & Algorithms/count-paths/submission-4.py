class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        level = [1] * n

        for j in range(m - 1):
            newLevel = [1] * n
            for i in range(n - 2, -1, -1):
                newLevel[i] = newLevel[i + 1] + level[i]
            level = newLevel
        
        return level[0]