class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Assume s[0] has locations a0 < a1 < ..., s[1] has locations b0 < b1 < ..., to make the subsequence possible, we should choose s[0] location a0, s[1] location bi where bi is the smallest location exceeding a0, and so on 
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == len(s)