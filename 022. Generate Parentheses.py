class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.dfs(n, n, result, "")
        return result
        
    def dfs(self, left, right, result, string):
        if right == 0:
            result.append(string)
        if left > 0:
            self.dfs(left-1, right, result, string+"(")
        if left < right:
            self.dfs(left, right-1, result, string+")")