class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # new occurs before i -> add it to res then add remaining
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                # new occurs after i (not overlapping)
                res.append(intervals[i])
            
            else:
                # new overlaps with i -> update new with merged new + i
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # if "new occurs before i" case was never hit, then new was never added to res
        res.append(newInterval)

        return res