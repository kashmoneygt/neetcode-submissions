class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        seen = set()  # course had been processed
        cycle = set() # tracking all courses along current DFS path
        
        def dfs(crs):
            if crs in cycle:
                return False # came back to the crs from 1 of its prereqs
            if crs in seen:
                return True # no need to visit course twice

            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False # a prereq is part of a cycle

            cycle.remove(crs) # no longer processing this course    
            seen.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): # incase graph is disjoint, run dfs from each course
                return False
        
        return True

            
