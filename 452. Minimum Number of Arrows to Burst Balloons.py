class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # O(nlogn) time, O(1) space
        points = sorted(points, key = lambda x: x[1])
        tail = float("-inf")
        size = 0
        for point in points:
            if point[0] > tail:
                tail = point[1]
                size += 1
        return size