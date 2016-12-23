class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # notice that all the elements in matrix are int
        # O(log(range(matrix))*n) time
        if len(matrix) == 0:
            return
        n = len(matrix)
        lower, upper = matrix[0][0], matrix[n-1][n-1]
        while lower < upper:
            mid = (lower+upper)//2
            count = 0  # number of matrix[i][j] <= mid
            j = n-1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j+1
            if count < k:
                lower = mid+1
            else:
                upper = mid
        return lower