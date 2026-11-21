class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for pre, crs in relations:
            adj[pre].append(crs)
        
        visited = {} # store -1 for visiting, and length of path for visited

        def dfs(cur):
            if cur in visited:
                return visited[cur]
            
            visited[cur] = -1 # mark as visiting

            max_len = 1
            for end in adj[cur]:
                length = dfs(end)
                if length == -1:
                    return 1 # hit a cycle
                
                max_len = max(max_len, length + 1)
            
            visited[cur] = max_len  # mark as visited
            return max_len
        

        max_len = -1
        for node in adj:
            length = dfs(node)
            if length == -1:
                return -1
            
            max_len = max(max_len, length)

        return max_len
