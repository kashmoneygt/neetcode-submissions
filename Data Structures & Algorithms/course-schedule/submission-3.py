class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i : [] for i in range(numCourses) }

        for pre, nei in prerequisites:
            adj[pre].append(nei)
        
        seen = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True

            cycle.add(crs)  
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            seen.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
