class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        freqs = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            freqs[count].append(num)
        
        res = []
        for i in range(len(freqs) -1, -1, -1):
            for num in freqs[i]:
                res.append(num)

                if len(res) == k:
                    return res
        