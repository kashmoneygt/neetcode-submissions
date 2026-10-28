class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxVal = max(stones)
        buckets = [0] * (maxVal + 1)
        for stone in stones:
            buckets[stone] += 1

        first = second = maxVal
        while first > 0:
            if buckets[first] % 2 == 0:
                first -= 1
                continue

            j = min(first - 1, second)
            while j > 0 and buckets[j] == 0:
                j -= 1

            if j == 0:
                return first

            second = j
            buckets[first] -= 1
            buckets[second] -= 1
            buckets[first - second] += 1
            first = max(first - second, second)

        return first