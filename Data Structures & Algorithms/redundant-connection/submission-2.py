class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            p = node
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(a, b):
            parentA, parentB = find(a), find(b)
            if parentA == parentB:
                return False

            if rank[parentB] > rank[parentA]:
                parent[parentA] = parentB
                rank[parentB] += rank[parentA]
            else:
                parent[parentB] = parentA
                rank[parentA] += rank[parentB]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
        