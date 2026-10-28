class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = { src: [] for src, dst in tickets }
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return res
            
            if src not in adj:
                return False
            
            outgoing = list(adj[src])
            for i, nei in enumerate(outgoing):
                adj[src].pop(i)
                res.append(nei)

                if dfs(nei):
                    return True
                
                adj[src].insert(i, nei)
                res.pop()
            
            return False

        dfs("JFK")
        return res
