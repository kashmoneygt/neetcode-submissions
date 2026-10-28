class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            p = node
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a, b):
            parentA, parentB = find(a), find(b)
            if parentA == parentB:
                return 0

            if rank[parentB] > rank[parentA]:
                parent[parentA] = parentB
                rank[parentB] += rank[parentA]
            else:
                parent[parentB] = parentA
                rank[parentA] += rank[parentB]
            return 1
        
        ccnum = n
        for a, b in edges:
            ccnum -= union(a, b)
        
        return ccnum