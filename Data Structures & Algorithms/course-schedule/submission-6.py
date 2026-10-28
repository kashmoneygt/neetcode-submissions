class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)
        
        def dfs(node, seen):
            if node in seen:
                return False
            
            seen.add(node)
            for nei in adj[node]:
                if not dfs(nei, seen):
                    return False
            
            seen.remove(node)
            adj[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True