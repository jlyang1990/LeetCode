class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        record = [[0]*n for i in range(m)]
        maxLen = 1
        for i in range(m):
            for j in range(n):
                if record[i][j] == 0:
                    maxLen = max(maxLen, self.helper(matrix, record, i, j))
        return maxLen
        
    
    def helper(self, matrix, record, i, j):
        if record[i][j] != 0:
            return record[i][j]
        # path will not go back since it is strictly increasing   
        record[i][j] = 1
        if i > 0 and matrix[i-1][j] > matrix[i][j]:
            record[i][j] = max(record[i][j], 1 + self.helper(matrix, record, i-1, j))
        if i < len(matrix)-1 and matrix[i+1][j] > matrix[i][j]:
            record[i][j] = max(record[i][j], 1 + self.helper(matrix, record, i+1, j))
        if j > 0 and matrix[i][j-1] > matrix[i][j]:
            record[i][j] = max(record[i][j], 1 + self.helper(matrix, record, i, j-1))
        if j < len(matrix[0])-1 and matrix[i][j+1] > matrix[i][j]:
            record[i][j] = max(record[i][j], 1 + self.helper(matrix, record, i, j+1))
        return record[i][j]