class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
                k -= 1

                if k == 0:
                    return res

        