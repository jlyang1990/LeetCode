# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        # O(nlogn) time
        startList = []
        result = []
        for i in range(len(intervals)):
            startList.append((intervals[i].start, i))
        startList = sorted(startList, key = lambda x: x[0])
        for i in range(len(intervals)):
            index = self.binarySearch(startList, intervals[i].end)
            if index == len(startList):
                result.append(-1)
            else:
                result.append(startList[index][1])
        return result
        
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid][0] < target:
                left = mid+1
            else:
                right = mid-1
        return left