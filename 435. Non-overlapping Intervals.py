# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # method 1
        # idea in longest increasing subsequence
        # O(nlogn) time, O(n) space
        intervals = sorted(intervals, key = lambda x: x.start)
        tails = [float("inf")] * len(intervals)
        size = 0
        for interval in intervals:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] <= interval.start:
                    i = m + 1
                else:
                    j = m
            tails[i] = min(interval.end, tails[i])
            size = max(i + 1, size)
        return len(intervals) - size
        
        # method 2
        # O(nlogn) time, O(1) space
        intervals = sorted(intervals, key = lambda x: x.end)
        tail = float("-inf")
        size = 0
        for interval in intervals:
            if interval.start >= tail:
                tail = interval.end
                size += 1
        return len(intervals) - size