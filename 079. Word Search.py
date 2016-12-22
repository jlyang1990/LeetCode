class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existHelper(board, word, 0, i, j):
                    return True
        return False
        
        
    def existHelper(self, board, word, k, i, j):
        if k == len(word):
            return True
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
            return False
        if board[i][j] != word[k]:
            return False
        temp = board[i][j]
        board[i][j] = "visited"
        result = self.existHelper(board, word, k+1, i-1, j) or self.existHelper(board, word, k+1, i+1, j) or \
        self.existHelper(board, word, k+1, i, j-1) or self.existHelper(board, word, k+1, i, j+1)
        board[i][j] = temp
        return result