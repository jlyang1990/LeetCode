class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.getFactorsHelper(n, 2, result, [])
        return result
        
        
    def getFactorsHelper(self, n, start, result, output):
        if n <= 1:
            if len(output) > 1:
                result.append(output)
        else:
            for i in range(start, n+1):
                if n % i == 0:
                    self.getFactorsHelper(n/i, i, result, output+[i])