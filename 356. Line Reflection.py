class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        minXVal, maxXVal = float("inf"), float("-inf")
        pointSet = set()
        for point in points:
            minXVal = min(minXVal, point[0])
            maxXVal = max(maxXVal, point[0])
            pointSet.add((point[0], point[1]))
        sumXVal = minXVal+maxXVal
        for point in points:
            if (sumXVal-point[0], point[1]) not in pointSet:
                return False
        return True