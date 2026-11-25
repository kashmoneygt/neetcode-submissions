class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = set()
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            
            if (row, col) in visited or grid[row][col] == 0:
                return

            visited.add((row, col))
            island.add((row - row_origin, col - col_origin))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                if island:
                    islands.add(frozenset(island))
            
        return len(islands)