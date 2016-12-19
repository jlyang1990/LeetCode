class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # size[i, j]: the maximum size of square with bottomright corner [i, j]
        # size[i, j] = matrix[i][j], if i = 0 or j = 0
        # size[i, j] = min(size[i-1, j-1], size[i-1, j], size[i, j-1])+1 if i > 0 and j > 0 and matrix[i][j] = 1
        # size[i, j] = 0 if i > 0 and j > 0 and matrix[i][j] = 0
        # O(mn) time, O(n) space
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        size = [0]*(n+1)
        maxsize = 0
        for i in range(m):
            pre = 0
            for j in range(n):
                temp = size[j+1]
                if matrix[i][j] == "1":
                    size[j+1] = min(pre, size[j+1], size[j]) + 1
                    maxsize = max(maxsize, size[j+1])
                else:
                    size[j+1] = 0
                pre = temp
        return maxsize**2