class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        unique_islands = set()

        # do a dfs to find all cells in current island
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            
            if (row, col) in visited or grid[row][col] == 0:
                return
            
            visited.add((row, col))
            current_island.add((row - row_origin, col - col_origin))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                if current_island:
                    unique_islands.add(frozenset(current_island))
        
        return len(unique_islands)
