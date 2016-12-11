class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # binary search
        # O(log(mn)) time
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = (left+right)/2
            if matrix[mid/n][mid%n] == target:
                return True
            elif matrix[mid/n][mid%n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False