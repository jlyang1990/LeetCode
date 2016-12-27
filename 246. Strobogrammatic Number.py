class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        left, right = 0, len(num)-1
        while left < right:
            if (num[left], num[right]) not in {("0", "0"), ("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")}:
                return False
            left += 1
            right -= 1
        if left == right and num[left] not in {"0", "1", "8"}:
            return False
        return True