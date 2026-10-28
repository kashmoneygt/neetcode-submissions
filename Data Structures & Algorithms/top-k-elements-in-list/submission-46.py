class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        counts = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            counts[freq].append(num)
        
        res = []
        for i in range(len(counts) - 1, -1, -1):
            for num in counts[i]:
                res.append(num)
                k -= 1

                if k == 0:
                    return res
        