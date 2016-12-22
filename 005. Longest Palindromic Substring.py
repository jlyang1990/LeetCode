class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n^2) time
        if len(s) == 0:
            return
        lower = 0
        maxlen = 1
        for i in range(len(s)-1):
            lower1, maxlen1 = self.extendPalindrome(s, i, i)
            lower2, maxlen2 = self.extendPalindrome(s, i, i+1)
            if maxlen1 > maxlen:
                lower, maxlen = lower1, maxlen1
            if maxlen2 > maxlen:
                lower, maxlen = lower2, maxlen2
        return s[lower:lower+maxlen]
        
    def extendPalindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i+1, j-i-1