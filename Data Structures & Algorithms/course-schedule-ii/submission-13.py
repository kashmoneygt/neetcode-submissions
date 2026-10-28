class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = { i : [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        output = []
        seen = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in seen:
                return True
            
            cycle.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            seen.add(crs)
            output.append(crs)
            
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return output

        

            
