class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        
        adj = { i : [] for i in range(n) }
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i) # b/c undirected
        
        visited = set()
        def dfs(cur, prev):
            if cur in visited:
                return False
            
            visited.add(cur)
            for nei in adj[cur]:
                if nei == prev:
                    continue
                if not dfs(nei, cur):
                    return False # nei is part of a cycle

            return True

        return dfs(0, -1) and len(visited) == n
