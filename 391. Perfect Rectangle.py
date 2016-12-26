class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # two conditions:
        # 1. counts of all the points except the corner points should be even, where counts of corner points should be 1
        # 2. summation of areas of small rectangles should equal to the area of large rectangles
        # O(n) time
        if len(rectangles) == 0 or len(rectangles[0]) == 0:
            return False
        left, right, top, bottom = float("inf"), float("-inf"), float("-inf"), float("inf")
        area = 0
        pointSet = set()
        for rect in rectangles:
            left, right, top, bottom = min(left, rect[0]), max(right, rect[2]), max(top, rect[3]), min(bottom, rect[1])
            area += (rect[2]-rect[0])*(rect[3]-rect[1])
            pointSet.add((rect[0], rect[1])) if (rect[0], rect[1]) not in pointSet else pointSet.remove((rect[0], rect[1]))
            pointSet.add((rect[0], rect[3])) if (rect[0], rect[3]) not in pointSet else pointSet.remove((rect[0], rect[3]))
            pointSet.add((rect[2], rect[1])) if (rect[2], rect[1]) not in pointSet else pointSet.remove((rect[2], rect[1]))
            pointSet.add((rect[2], rect[3])) if (rect[2], rect[3]) not in pointSet else pointSet.remove((rect[2], rect[3]))
        return pointSet == {(left, bottom), (left, top), (right, bottom), (right, top)} and area == (right-left)*(top-bottom)