class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # same[i]: total number of ways until i where the last two colors are the same
        # diff[i]: total number of ways until i where the last two colors are different
        # same[i] = diff[i-1]
        # diff[i] = (same[i-1]+diff[i-1])*(k-1)
        # same[0] = 0, diff[0] = k
        # O(n) time, O(1) space
        if n == 0:
            return 0
        same, diff = 0, k
        for i in range(1, n):
            same, diff = diff, (same+diff)*(k-1)
        return same + diff