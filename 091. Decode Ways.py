class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # O(n) time, O(1) space
        if len(s) == 0 or s[0] == "0":
            return 0
        previous, current = 1, 1
        for i in range(1, len(s)):
            temp = 0
            if s[i] != "0":
                temp += current
            if s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) <= 6):
                temp += previous
            if temp == 0:
                return 0
            previous, current = current, temp
        return current