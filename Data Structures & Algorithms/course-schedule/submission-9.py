class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if not adj[node]:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visited.remove(node)
            adj[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True