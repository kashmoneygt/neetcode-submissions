class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]] # populate with 1st interval

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                # we overlap with last -> update last to include us
                res[-1][1] = max(lastEnd, end)
            else:
                # we don't overlap with last
                res.append([start, end])
        
        return res



