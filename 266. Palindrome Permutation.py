class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charSet = set()
        for i in s:
            if i not in charSet:
                charSet.add(i)
            else:
                charSet.remove(i)
        return len(charSet) in {0, 1}