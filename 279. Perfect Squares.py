class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dynamic programming
        # O(n^3/2) time, O(n) space
        nList = [float("inf")]*n
        for i in range(1, int(n**0.5)+1):
            nList[i**2-1] = 1
            for j in range(i**2, n):
                nList[j] = min(nList[j], nList[j-i**2]+1)
        return nList[n-1]