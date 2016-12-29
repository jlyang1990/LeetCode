class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        usedRow = [set() for i in range(9)]
        usedCol = [set() for i in range(9)]
        usedBlock = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    k = i // 3 * 3 + j // 3
                    if board[i][j] in usedRow[i] or board[i][j] in usedCol[j] or board[i][j] in usedBlock[k]:
                        return False
                    usedRow[i].add(board[i][j])
                    usedCol[j].add(board[i][j])
                    usedBlock[k].add(board[i][j])
        return True