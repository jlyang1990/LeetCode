class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            for i in range(numRows-2):
                result.append([1]+[result[-1][i]+result[-1][i+1] for i in range(len(result[-1])-1)]+[1])
        return result