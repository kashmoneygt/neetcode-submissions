class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i: i[0])
        
        minHeap = [] # store (size, right) tuples
        res = {}     # store query -> size of its min interval
        i = 0        # tracks where we are in intervals

        for q in sorted(queries):
            
            # Add all intervals this query CAN be a part of (start <= q)
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r)) # size = r - l + 1
                i += 1
            
            # Remove all intervals this query CAN'T be a part of (right < q)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Get smallest interval
            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]
