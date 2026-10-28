class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visit / processing set - all courses along current DFS path
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False # came back to the crs from 1 of its prereqs
            if len(preMap[crs]) == 0:
                return True # no prereqs remaining
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False # a prereq is part of a cycle

            visit.remove(crs) # no longer processing this course    
            preMap[crs] = [] # if called again, we know its prereqs can be completed
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

            
