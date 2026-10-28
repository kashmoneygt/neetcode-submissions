class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")
        
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2

            total = 0
            for p in piles:
                total += math.ceil(float(p) / mid)
            
            if total <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res