"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0 # res tracks max count
        s, e = 0, 0 # s in start, e in end
        while s < len(intervals):
            if start[s] < end[e]:
                # if end > start, process start
                s += 1
                count += 1
            else:
                # if end > start or end == start, process end
                e += 1
                count -= 1

            res = max(res, count)

        return res
