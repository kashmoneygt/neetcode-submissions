class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1): # find parent of node
            res = n1
            while res != parent[res]:
                # path compression: set our parent to our grandparent
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2) -> bool:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0 # did not perform a union
            
            if rank[p2] > rank[p1]: # add p1 to p2
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        ccnum = n
        for n1, n2 in edges:
            ccnum -= union(n1, n2)
        return ccnum

