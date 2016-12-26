class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # hp[i, j]: minimum hp needed at [i, j]
        # hp[i, j] = max(min(hp[i+1, j], hp[i, j+1]) - dungeon[i, j], 1)
        # hp[m, j] = inf, hp[i, n] = inf, hp[m][n-1] = 1 (need to be alive at dungeon[m-1][n-1])
        # O(mn) time, O(n) space
        if len(dungeon) == 0:
            return
        m, n = len(dungeon), len(dungeon[0])
        hp = [float("inf")]*(n+1)
        hp[n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                hp[j] = max(min(hp[j+1], hp[j])-dungeon[i][j], 1)
        return hp[0]