# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # O(n^2) time
        maxPoints = 0
        for i in range(len(points)):
            pointsDic = {}
            samePoints = 0
            for j in range(len(points)):
                if j != i:
                    if points[j].x == points[i].x and points[j].y == points[i].y:
                        samePoints += 1
                    elif points[j].x == points[i].x:
                        if float("inf") not in pointsDic:
                            pointsDic[float("inf")] = 1
                        else:
                            pointsDic[float("inf")] += 1
                    else:
                        sloap = float(points[j].y-points[i].y)/(points[j].x-points[i].x)
                        if sloap not in pointsDic:
                            pointsDic[sloap] = 1
                        else:
                            pointsDic[sloap] += 1
            maxPoints = max(maxPoints, 1+samePoints)
            for sloap in pointsDic:
                maxPoints = max(maxPoints, pointsDic[sloap]+1+samePoints)
        return maxPoints