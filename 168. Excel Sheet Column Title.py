class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            result += chr((n-1)%26 + ord("A"))
            n = (n-1)/26
        return result[::-1]