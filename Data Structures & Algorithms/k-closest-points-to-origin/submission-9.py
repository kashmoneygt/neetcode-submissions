class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2

        def quickSelect(l, r):
            p, pivot = l, euclidean(points[r])
            for i in range(l, r):
                if euclidean(points[i]) <= pivot:
                    points[p], points[i] = points[i], points[p]
                    p += 1
            
            points[p], points[r] = points[r], points[p]
            return p
        
        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = quickSelect(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]
