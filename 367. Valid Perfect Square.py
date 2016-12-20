class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        current = 1
        while num > 0:
            num -= current
            current += 2
        return num == 0