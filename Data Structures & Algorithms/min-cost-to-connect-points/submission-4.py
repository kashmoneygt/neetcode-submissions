class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = { i : [] for i in range(N) } # map index to (cost, point index)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))


        res = 0
        visited = set()
        minHeap = [(0, 0)] # hold (cost, point index)
        while len(visited) < N:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue

            res += cost
            visited.add(node)

            for neiCost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiCost, nei))
        
        return res
