class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            x = -x
            negative = True
        result = 0
        while x > 0:
            result = result*10+x%10
            x /= 10
        if result >= 2147483647:
            return 0
        if negative:
            result = -result
        return result