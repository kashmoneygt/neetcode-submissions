class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # we don't have enough equations to determine the value of each variable
        # we have [a,b] and [b,c] with query = [a,c]
        # so we can start at a/b and figure out how we can get closer to a/c
        # map every enumerator to all the denominators (a -> b -> c). should also be able to go from c to a so map denom->num as well
        # N*(V+E) / V+E (the graph)
        adj = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i])) # inverse of a/b

        
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q, visit = deque(), set()
            q.append((src, 1)) # keep track of value so far for every path we take
            visit.add(src)

            while q:
                node, val = q.popleft()
                if node == target:
                    return val
                
                for nei, nei_val in adj[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, val * nei_val))

            return -1 # no path between src and target

        return [bfs(src, target) for src, target in queries]
