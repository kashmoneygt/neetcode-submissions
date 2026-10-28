class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting - nlogn / n
        # heap - pop k times - nlogk / n+k
        # bucket sort - hashmap to find counts, use counts in buckets - n / n
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: return res
        
