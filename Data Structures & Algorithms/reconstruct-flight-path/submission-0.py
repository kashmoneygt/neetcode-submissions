class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort() # will sort by pair[0] then pair[1]
        adj = { src: [] for src, dst in tickets }
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return res
            
            # no outgoing edges, got stuck so backtrack
            if src not in adj: 
                return False
            
            # create a copy b/c we'll be updating the adj list
            temp = list(adj[src]) 
            for i, nei in enumerate(temp):
                adj[src].pop(i)
                res.append(nei)

                if dfs(nei):
                    return True
                
                # nei got stuck so add it back to adj and remove from res
                adj[src].insert(i, nei)
                res.pop()
            
            return False

        dfs("JFK")
        return res                

