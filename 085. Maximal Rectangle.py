class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # maximal rectangle at matrix[i][j]: height[i][j] * (right[i][j] - left[i][j])
        # height[i][j] = height[i-1][j] + 1 if matrix[i][j] = 1 else 0
        # left[i][j] = max(left[i-1][j], curLeft)
        # right[i][j] = min(right[i-1][j], curRight)
        # O(mn) time, O(n) space
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        height, left, right = [0]*n, [0]*n, [n]*n
        maxArea = 0
        for i in range(m):
            curLeft, curRight = 0, n
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], curLeft)
                else:
                    left[j] = 0  # reset left[j], will not affect maxArea since height[j] = 0
                    curLeft = j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], curRight)
                else:
                    right[j] = n  # reset right[j], will not affect maxArea since height[j] = 0
                    curRight = j
            for j in range(n):
                maxArea = max(maxArea, height[j]*(right[j]-left[j]))
        return maxArea