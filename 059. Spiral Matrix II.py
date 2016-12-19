class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)]
        row_start, row_end, col_start, col_end = 0, n-1, 0, n-1
        current = 1
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end+1):
                matrix[row_start][i] = current
                current += 1
            row_start += 1
            for j in range(row_start, row_end+1):
                matrix[j][col_end] = current
                current += 1
            col_end -= 1
            if row_start <= row_end:
                for i in range(col_end, col_start-1, -1):
                    matrix[row_end][i] = current
                    current += 1
                row_end -= 1
            if col_start <= col_end:
                for j in range(row_end, row_start-1, -1):
                    matrix[j][col_start] = current
                    current += 1
                col_start += 1
        return matrix