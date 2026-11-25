class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        for i, (a, b) in enumerate(equations):
            adj.setdefault(a, []).append((b, values[i]))
            adj.setdefault(b, []).append((a, 1 / values[i]))
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            if src == target:
                return 1

            q = collections.deque([(src, 1)])
            visited = set()
            while q:
                node, val = q.popleft()
                if node in visited:
                    continue
                if node == target:
                    return val
                
                visited.add(node)
                for nei, nei_val in adj.get(node, []):
                    q.append((nei, val * nei_val))
            
            return -1



        res = []
        for query in queries:
            res.append(bfs(query[0], query[1]))
        return res