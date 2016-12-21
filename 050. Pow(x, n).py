class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x**2, n//2)
        if n % 4 == 1:
            return x*self.myPow(x, n-1)
        if n % 4 == 3:
            return 1/x*self.myPow(x, n+1)