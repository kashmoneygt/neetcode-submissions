class UnionFind:
    def __init__(self, n: int):
        self.rank = [1] * n
        self.parent = [-1] * n
        self.count = 0

    def add(self, n1):
        if self.parent[n1] >= 0:
            return
        self.parent[n1] = n1
        self.count += 1

    def is_land(self, n1):
        return self.parent[n1] >= 0

    def find(self, n1):
        while n1 != self.parent[n1]:
            self.parent[n1] = self.parent[self.parent[n1]]
            n1 = self.parent[n1]
        return n1

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.count -= 1
    


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        dsu = UnionFind(m * n)
        answer = []

        for r, c in positions:
            index = r * n + c
            dsu.add(index)

            for x, y in dirs:
                nei_x = r + x
                nei_y = c + y
                nei_index = nei_x * n + nei_y

                if nei_x >= 0 and nei_x < m and nei_y >= 0 and nei_y < n and dsu.is_land(nei_index):
                    dsu.union(index, nei_index)
            
            answer.append(dsu.count)

        return answer