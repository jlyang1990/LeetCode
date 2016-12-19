class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        # O(mn) time, O(mn) space
        if len(matrix) == 0:
            self.cummatrix = []
        else:
            m, n = len(matrix), len(matrix[0])
            self.cummatrix = [[0]*(n+1) for i in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    self.cummatrix[i][j] = matrix[i-1][j-1] + self.cummatrix[i-1][j] + self.cummatrix[i][j-1] - self.cummatrix[i-1][j-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # O(1) time
        if len(self.cummatrix) == 0:
            return None
        return self.cummatrix[row2+1][col2+1] - self.cummatrix[row2+1][col1] - self.cummatrix[row1][col2+1] + self.cummatrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)