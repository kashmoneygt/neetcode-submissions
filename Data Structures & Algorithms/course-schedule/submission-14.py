class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # similar to a visited set for globally seen nodes, but cycle detection requires local path
        path = set() # all the courses along the current DFS path
        def dfs(crs):
            if crs in path:
                return False # cycle: node is in current recursion path
            if preMap[crs] == []:
                return True  # already processed, no cycle
            
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            path.remove(crs)
            preMap[crs] = [] # mark as processed, so we don't have to repeat work
            return True

        # need to check all courses rather than only from course 0
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
