class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n = abcdefg, consider the occurrence of one on thousand
        # abc*1000, if d = 0
        # abc*1000+efg+1, if d = 1
        # abc*1000+1000, if d > 1
        current, multiplier, result = n, 1, 0
        while current > 0:
            digit = current % 10
            current /= 10
            result += current * multiplier
            if digit == 1:
                result += n % multiplier + 1
            elif digit > 1:
                result += multiplier
            multiplier *= 10
        return result