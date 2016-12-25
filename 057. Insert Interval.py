# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # O(n) time
        result = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i].end < newInterval.start:
            result.append(intervals[i])
            i += 1
        newInt = Interval(newInterval.start, newInterval.end)
        while i < n and intervals[i].start <= newInterval.end:
            newInt.start = min(newInt.start, intervals[i].start)
            newInt.end = max(newInt.end, intervals[i].end)
            i += 1
        result.append(newInt)
        while i < n:
            result.append(intervals[i])
            i += 1
        return result