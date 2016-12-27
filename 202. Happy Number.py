class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numSet = {n}
        num = n
        while num != 1:
            num = self.getHappy(num)
            if num in numSet:
                return False
            numSet.add(num)
        return True
        
        
    def getHappy(self, n):
        result = 0
        while n > 0:
            result += (n%10)**2
            n /= 10
        return result