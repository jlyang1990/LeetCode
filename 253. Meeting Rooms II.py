# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # go through timeline
        # O(nlogn) time
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])
        i, j = 0, 0
        roomNum, roomEmptyNum = 0, 0
        while i < len(starts):
            if starts[i] < ends[j]:  # a meeting starts
                if roomEmptyNum == 0:
                    roomNum += 1
                else:
                    roomEmptyNum -= 1
                i += 1
            else:  # a meeting ends
                roomEmptyNum += 1
                j += 1
        return roomNum