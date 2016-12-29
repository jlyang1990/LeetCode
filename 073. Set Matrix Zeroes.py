class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # set matrix[0][j] = 0 if column j contains 0, 0<=j<=n-1
        # set matrix[i][0] = 0 if row i contains 0, 1<=i<=m-1, set row0 = 0 if row 0 contains 0
        # O(mn) time, O(1) space
        if len(matrix) == 0:
            return
        m, n = len(matrix), len(matrix[0])
        row0 = 1
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = 0
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(m-1, 0, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0 == 0:
            for j in range(n):
                matrix[0][j] = 0