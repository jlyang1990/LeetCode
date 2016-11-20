class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # dynamic programming
        m = len(grid)
        n = len(grid[0])
        sum_grid = []
        for j in range(m):
            sum_grid.append([None]*n)
        sum_grid[0][0] = grid[0][0]
        for i in range(1, n):
            sum_grid[0][i] = sum_grid[0][i-1] + grid[0][i]
        for j in range(1, m):
            sum_grid[j][0] = sum_grid[j-1][0] + grid[j][0]
        for j in range(1, m):
            for i in range(1, n):
                sum_grid[j][i] = min(sum_grid[j-1][i], sum_grid[j][i-1]) + grid[j][i]
        return sum_grid[m-1][n-1]