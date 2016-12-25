class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # water flows back from ocean to land
        # dfs
        # O(mn) time, O(mn) space
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        pacificVisited = [[False]*n for i in range(m)]
        atlanticVisited = [[False]*n for i in range(m)]
        for i in range(m):
            self.pacificAtlanticHelper(matrix, pacificVisited, float("-inf"), i, 0)
            self.pacificAtlanticHelper(matrix, atlanticVisited, float("-inf"), i, n-1)
        for j in range(n):
            self.pacificAtlanticHelper(matrix, pacificVisited, float("-inf"), 0, j)
            self.pacificAtlanticHelper(matrix, atlanticVisited, float("-inf"), m-1, j)
        result = []
        for i in range(m):
            for j in range(n):
                if pacificVisited[i][j] and atlanticVisited[i][j]:
                    result.append([i, j])
        return result
        
        
    def pacificAtlanticHelper(self, matrix, visited, height, i, j):
        if i in [-1, len(matrix)] or j in [-1, len(matrix[0])] or visited[i][j] or matrix[i][j] < height:
            return
        visited[i][j] = True
        self.pacificAtlanticHelper(matrix, visited, matrix[i][j], i-1, j)
        self.pacificAtlanticHelper(matrix, visited, matrix[i][j], i+1, j)
        self.pacificAtlanticHelper(matrix, visited, matrix[i][j], i, j-1)
        self.pacificAtlanticHelper(matrix, visited, matrix[i][j], i, j+1)