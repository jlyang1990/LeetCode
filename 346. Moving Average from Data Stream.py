class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        import Queue
        self.queue = Queue.Queue(size)
        self.MovingSum = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # O(1) time
        if self.queue.full():
            self.MovingSum += val - self.queue.get()
        else:
            self.MovingSum += val
        self.queue.put(val)
        return float(self.MovingSum) / self.queue.qsize()


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)