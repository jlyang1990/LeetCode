class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 3:
            return 2
        if n%2 == 0:
            return 1+self.integerReplacement(n/2)
        if n%4 == 1:
            return 1+self.integerReplacement(n-1)
        if n%4 == 3:
            return 1+self.integerReplacement(n+1)