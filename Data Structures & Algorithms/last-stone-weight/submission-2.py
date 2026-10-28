class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            diff = first - second
            if second > first:
                heapq.heappush(stones, first - second)
        
        return abs(stones[0]) if stones else 0