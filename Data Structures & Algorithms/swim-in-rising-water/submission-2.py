class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set((0, 0)) # start from (0, 0)
        minHeap = [(grid[0][0], 0, 0)] # (max time, r, c)

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            visited.add((r, c))
            
            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in dirs:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visited):
                    continue
                
                maxT = max(t, grid[neiR][neiC])
                heapq.heappush(minHeap, (maxT, neiR, neiC))
