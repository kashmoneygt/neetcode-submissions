class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = collections.defaultdict(list) # manager -> [employees]
        for i in range(n):
            adj[manager[i]].append(i)

        # no need for visited since this is just a tree
        q = collections.deque()
        q.append((headID, 0))

        res = 0
        while q:
            node, time = q.popleft()
            res = max(res, time)
            for employee in adj[node]:
                q.append((employee, time + informTime[node]))
    
        return res
