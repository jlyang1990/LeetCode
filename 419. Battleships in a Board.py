class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # in one-pass, using only O(1) extra memory and without modifying the value of the board
        # pick the topleft "X" as the representative of a battleship
        m = len(board)
        n = len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                    count += 1
        return count