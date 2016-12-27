class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # O(mn) time, O(n) space 
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        maxEnemies = 0
        colEnemies = [0]*n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j-1] == "W":
                    rowEnemies = 0
                    k = j
                    while k < n and grid[i][k] != "W":
                        rowEnemies += grid[i][k] == "E"
                        k += 1
                if i == 0 or grid[i-1][j] == "W":
                    colEnemies[j] = 0
                    k = i
                    while k < m and grid[k][j] != "W":
                        colEnemies[j] += grid[k][j] == "E"
                        k += 1
                if grid[i][j] == "0":
                    maxEnemies = max(maxEnemies, rowEnemies+colEnemies[j])
        return maxEnemies