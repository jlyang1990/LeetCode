class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        j = 0
        while j < n and obstacleGrid[0][j] == 0:
            j += 1
        grid = [[1]*j+[0]*(n-j)]
        i = 0
        while i < m and obstacleGrid[i][0] == 0:
            i += 1
        temp = [1]*i+[0]*(m-i)
        for i in range(1, m):
            grid.append([temp[i]]+[None]*(n-1))
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
        return grid[m-1][n-1]