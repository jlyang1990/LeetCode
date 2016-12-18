from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Max-heap "small" has the smaller half of numbers
        # Min-heap "large" has the larger half of numbers
        self.heap = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # O(logn) time
        small, large = self.heap
        heappush(small, -heappushpop(large, num))
        if len(small)-len(large) > 1:
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # O(1) time
        small, large = self.heap
        if len(small) > len(large):
            return -small[0]
        else:
            return (large[0]-small[0])/2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()