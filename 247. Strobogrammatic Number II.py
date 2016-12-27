class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n%2 == 0:
            self.dfs(n, result, "")
        else:
            self.dfs(n-1, result, "0")
            self.dfs(n-1, result, "1")
            self.dfs(n-1, result, "8")
        return result
            
            
    def dfs(self, n, result, num):
        if n == 0:
            result.append(num)
        else:
            if n-2 > 0:
                self.dfs(n-2, result, "0"+num+"0")
            self.dfs(n-2, result, "1"+num+"1")
            self.dfs(n-2, result, "8"+num+"8")
            self.dfs(n-2, result, "6"+num+"9")
            self.dfs(n-2, result, "9"+num+"6")