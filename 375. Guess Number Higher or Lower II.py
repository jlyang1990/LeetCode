class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # pay[i][j] = 0, if i >= j
        # pay[i][j] = min_{i<=k<j} k + max(pay[i][k-1], pay[k+1][j])
        # O(n^3) time, O(n^2) space
        pay = [[0]*n for i in range(n)]
        for l in range(1, n):
            for i in range(n-l):
                j = i+l
                pay[i][j] = i+1+pay[i+1][j]
                for k in range(i+1, j):
                    pay[i][j] = min(pay[i][j], k+1+max(pay[i][k-1], pay[k+1][j]))
        return pay[0][n-1]