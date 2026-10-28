class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []        # output from topo sort
        visited = set()    # course had been added to output
        cycle = set()      # tracking all courses along current DFS path
        
        def dfs(crs):
            if crs in cycle:
                return False # came back to the crs from 1 of its prereqs
            if crs in visited:
                return True # no need to visit course twice

            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False # a prereq is part of a cycle


            cycle.remove(crs) # no longer processing this course    
            visited.add(crs)
            output.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs): # incase graph is disjoint, run dfs from each course
                return []
        
        return output
