class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # a course has 3 possible states
        # 1) visited -> crs has been added to output
        # 2) visiting -> crs not added to output, but added to path
        # 3) visited -> crs not added to output or path
        output = []
        visited, path = set(), set()
        def dfs(crs) -> bool:
            if crs in path: # currently in path -> cycle
                return False
            if crs in visited: # already processed -> skip
                return True
            
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            path.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return output