class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # split the matrix into four parts: topleft, topright, bottomright, bottomleft
        # topright, bottomright, bottomleft, topleft = topleft, topright, bottomright, bottomleft
        n = len(matrix)
        for i in range(n/2):
            for j in range((n+1)/2):
                matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i], matrix[i][j] \
                = matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i]