class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        result = []
        row_start, row_end, col_start, col_end = 0, len(matrix)-1, 0, len(matrix[0])-1
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end+1):
                result.append(matrix[row_start][i])
            row_start += 1
            for j in range(row_start, row_end+1):
                result.append(matrix[j][col_end])
            col_end -= 1
            if row_start <= row_end:
                for i in range(col_end, col_start-1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1
            if col_start <= col_end:
                for j in range(row_end, row_start-1, -1):
                    result.append(matrix[j][col_start])
                col_start += 1
        return result