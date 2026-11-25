class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        res = []
        visited, path = set(), set()
        def dfs(node):
            if node in path:
                return False # part of cycle
            if node in visited:
                return True # already processed
            
            path.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False

            path.remove(node)
            res.append(node)
            visited.add(node)
            return True
        
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res