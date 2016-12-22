class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # knowledge of combinatorics
        # O(n) time, O(1) space
        if n == 0:
            return 1
        if n > 9:
            n = 9
        count = 9
        total = 10
        for i in range(1, n):
            count *= (10-i)
            total += count
        return total