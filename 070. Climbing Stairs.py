class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fibonacci
        current = 1
        previous = 1
        for i in range(n-1):
            current, previous = current+previous, current
        return current