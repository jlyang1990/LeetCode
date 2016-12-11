class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.sink(grid, i, j)
                    num += 1
        return num
        
    def sink(self, grid, row, col):
        if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == "1":
            grid[row][col] = "0"
            self.sink(grid, row-1, col)
            self.sink(grid, row+1, col)
            self.sink(grid, row, col-1)
            self.sink(grid, row, col+1)