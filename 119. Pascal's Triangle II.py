class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # the kth row of the Pascal's triangle is combination numbers [(k, 0), (k, 1), ..., (k, k)]
        # O(k) time
        result = [1]*(rowIndex+1)
        for i in range(1, rowIndex+1):
            result[i] = result[i-1] * (rowIndex-i+1) / i
        return result