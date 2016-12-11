class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # path_sum: minimum path sum to each element in layer i
        # O(n^2) time, O(n) space
        n = len(triangle)
        path_sum = [0]+[float("inf")]*(n-1)
        for i in range(n):
            for j in range(i, 0, -1):
                path_sum[j] = triangle[i][j] + min(path_sum[j-1], path_sum[j])
            path_sum[0] = triangle[i][0] + path_sum[0]
        return min(path_sum)